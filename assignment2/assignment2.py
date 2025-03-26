import csv
import os
import custom_module
from datetime import datetime


# Task 2: Read a CSV File
def read_employees():
    rows =[]
    employees_dict = {}
    try:
        with open('../csv/employees.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            first_row = True
            for row in reader:
                if first_row:
                    employees_dict["fields"] = row
                    first_row = False
                else:
                    rows.append(row)
            employees_dict["rows"] = rows
        return employees_dict      
    except Exception as e:
        print(f'An error occurred while processing the file: {e}')
        

employees = read_employees()
print("employees: ", employees)

# Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

# Task 4: Find the Employee First Name
def first_name(row_number):
    first_name_index = column_index("first_name")
    return employees["rows"][row_number][first_name_index]

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees["rows"].sort(key=lambda row : row[last_name_index])
    return employees["rows"]
sort_by_last_name()
print('employees',employees)

# Task 8: Create a dict for an Employee
def employee_dict(row):
    keys = employees["fields"][1:]
    values = row[1:] 
    new_dict = {}
    for i in range(len(keys)):
        new_dict[keys[i]]=values[i]
    return new_dict

print('employee_dict', employee_dict(employees["rows"][10]))

# Second option with zip function
# def employee_dict(row):
#     keys = employees["fields"][1:]
#     values = row[1:] 
#     return dict(zip(keys, values))
# print('employee_dict', employee_dict(employees["rows"][10]))



# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    return { row[0]: employee_dict(row) for row in employees["rows"] }
print(all_employees_dict())

# Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11: Creating Your Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
set_that_secret("top secret info")
print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv

def read_minutes():
    minutes1, minutes2 = dict(), dict()
    new_list = []
    with open('../csv/minutes1.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(tuple(row))
        minutes1["fields"] = new_list[0]
        minutes1["rows"] = new_list[1:]
    new_list = []
    with open('../csv/minutes2.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(tuple(row))
        minutes2["fields"] = new_list[0]
        minutes2["rows"] = new_list[1:]
    return minutes1, minutes2    

minutes1, minutes2 = read_minutes()
print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)



# Option without repeating the code "DRY"

# def read_minutes():
#     def file_reader(file_name):
#         min_dict = {}
#         rows = []
#         with open(file_name, 'r', newline='') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 rows.append(tuple(row))
#             min_dict["fields"] = rows[0]
#             min_dict["rows"] = rows[1:]
#             return min_dict
#     minutes1 = file_reader("../csv/minutes1.csv")
#     minutes2 = file_reader("../csv/minutes2.csv")
#     return minutes1, minutes2    

# minutes1, minutes2 = read_minutes()
# print("Minutes 1:", minutes1)
# print("Minutes 2:", minutes2)

# Task 13: Create minutes_set
def create_minutes_set():
    set_minutes1 = set(minutes1["rows"])
    set_minutes2 = set(minutes2["rows"])
    return set_minutes1.union(set_minutes2)
minutes_set = create_minutes_set()
print("minutes_set", minutes_set)

# Task 14: Convert to datetime
def create_minutes_list():
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
minutes_list = create_minutes_list()
print("minutes_list", minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
    sorted_minutes = sorted(minutes_list, key=lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sorted_minutes))
    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerow(converted_list)
    return converted_list

write_sorted_list()