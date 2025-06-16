import pandas as pd
import json

# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames

# 1.1 Create a DataFrame from a dictionary:
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)


# 1.2 Add a new column:
task1_data_frame = df

task1_with_salary = df.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

# 1.3 Modify an existing column:
task1_older = task1_with_salary.copy()
task1_older['Age'] +=1
print(task1_older)

# 1.4 Save the DataFrame as a CSV file:
task1_older.to_csv("employees.csv", index=False)


# Task 2: Loading Data from CSV and JSON

# 2.1 Read data from a CSV file:
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

# 2.2 Read data from a JSON file:
data = {
    'Name': ['Eve', 'Frank'],
    'Age': [28, 40],
    'City': ['Miami', 'Seattle'],
    'Salary': [60000, 95000]
}
with open("additional_employees.json", "w") as file:
    json.dump(data, file, indent=4)

json_employees = pd.read_json('additional_employees.json')
print(json_employees)

# 2.3.Combine DataFrames:
more_employees = pd.concat([task2_employees,json_employees], ignore_index=True)
print(more_employees)


# Task 3: Data Inspection - Using Head, Tail, and Info Methods

# 3.1 Use the head() method:
first_three = more_employees.head(3)
print(first_three)

# 3.2 Use the tail() method:
last_two = more_employees.tail(2)
print(last_two)

# 3.3 Get the shape of a DataFrame
employee_shape = more_employees.shape
print(employee_shape)

# 3.4 Use the info() method:
print(more_employees.info())

# Task 4: Data Cleaning

# 4.1 Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data.
dirty_data = pd.read_csv('dirty_data.csv')
print(dirty_data)
clean_data = dirty_data.copy()

# 4.2 Remove any duplicate rows from the DataFrame
clean_data = clean_data.drop_duplicates()
print(clean_data)

# 4.3 Convert Age to numeric and handle missing values
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print(clean_data)

# 4.4 Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print(clean_data)

# 4.5 Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median
mean_age = clean_data["Age"].mean()
median_salary = clean_data["Salary"].median()
clean_data["Age"] = clean_data["Age"].fillna(mean_age)
clean_data["Salary"] = clean_data["Salary"].fillna(median_salary)
print(clean_data)

# 4.6 Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
print(clean_data)

# 4.7 Strip extra whitespace and standardize Name and Department as uppercase
clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Department"] = clean_data["Department"].str.strip()

clean_data["Name"] = clean_data["Name"].str.upper()
clean_data["Department"] = clean_data["Department"].str.upper()

print(clean_data)