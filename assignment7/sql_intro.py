import sqlite3

def add_publisher(cursor, publisher_name):
    try:
        cursor.execute("INSERT INTO Publishers (publisher_name) VALUES (?)", (publisher_name,))
    except sqlite3.IntegrityError:
        print(f"Publisher {publisher_name} is already in the database.")

def add_magazine(cursor, magazine_name, publisher_id):
    try:
        cursor.execute("INSERT INTO Magazines (magazine_name, publisher_id) VALUES (?,?)", (magazine_name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"Magazine {magazine_name} is already in the database.")

def add_subscriber(cursor, subscriber_name, subscriber_address):
    try:
        cursor.execute("SELECT * FROM subscribers WHERE subscriber_name = ? AND subscriber_address = ?", (subscriber_name, subscriber_address))
        if cursor.fetchone():
            print(f"Subscriber {subscriber_name} at {subscriber_address} is already in the database.")
        else:
            cursor.execute("INSERT INTO Subscribers (subscriber_name, subscriber_address) VALUES (?, ?)", (subscriber_name, subscriber_address))
    except sqlite3.Error as e:
        print(f"Error adding subscriber: {e}")

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute("INSERT INTO Subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date))
    except sqlite3.Error as e:
        print(f"Error adding subscription: {e}")

try:    
    with  sqlite3.connect("../db/magazines.db") as conn: 
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Publishers (
                publisher_id INTEGER PRIMARY KEY,
                publisher_name TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Magazines (
                magazine_id INTEGER PRIMARY KEY,
                magazine_name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Subscribers (
                subscriber_id INTEGER PRIMARY KEY,
                subscriber_name TEXT NOT NULL,
                subscriber_address TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Subscriptions (
                subscription_id INTEGER PRIMARY KEY,
                magazine_id INTEGER NOT NULL,
                subscriber_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                FOREIGN KEY (magazine_id) REFERENCES Magazines(magazine_id),
                FOREIGN KEY (subscriber_id) REFERENCES Subscribers(subscriber_id)
            )
        """)

    add_publisher(cursor, "Everbodys")
    add_publisher(cursor, "Whoknows")
    add_publisher(cursor,"Fancy shmancy")

    add_magazine(cursor, "The New Yorker", 1)
    add_magazine(cursor, "Life", 2)
    add_magazine(cursor, "Vogue", 3)

    add_subscriber(cursor, "Allen Apple", "123 Manhattan St")
    add_subscriber(cursor, "Jimmy Young", '345 Forever Young St')
    add_subscriber(cursor, "Bruce Broce", "777 Karate St")

    add_subscription(cursor, 1, 1, "2025-12-31")
    add_subscription(cursor, 2, 2, "2035-01-01")
    add_subscription(cursor, 3, 3, "2027-03-09")
        
    conn.commit()
    print("Database populated successfully.")

    cursor.execute("SELECT * FROM Subscribers")
    result = cursor.fetchall()
    print("Subscribers: ")
    for row in result:
        print(row)

    cursor.execute("SELECT * FROM Magazines ORDER BY magazine_name")
    result = cursor.fetchall()
    print("\n Magazines:")
    for row in result:
        print(row)

    publisher_id = 1
    cursor.execute("""SELECT m.magazine_name FROM Magazines m JOIN Publishers p ON m.publisher_id = p.publisher_id WHERE p.publisher_id = ?""", (publisher_id,))

    result = cursor.fetchall()
    print("\n Magazines by Publisher {publisher_id}:")
    for row in result:
        print(row)

    print("Tables created successfully.")
except sqlite3.Error as e:
    print(f"Error creating database: {e}")