import csv
import os
from time import sleep


os.system("cls")

EMPLOYEE_FILE = 'employees.csv'


def initialize_employee_file():

    if not os.path.exists(EMPLOYEE_FILE):
        with open(EMPLOYEE_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'First Name', 'Last Name', 'Position', 'Salary', 'Department', 'Programming Language'])


def get_next_employee_id():
   
    with open(EMPLOYEE_FILE, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        if len(rows) > 1:
            last_id = int(rows[-1][0])
            return last_id + 1
        else:
            return 1


def add_employee():
    
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")
    department = input("Enter Department: ")
    programming_language = input("Enter your Programming Language: ")

    employee_id = get_next_employee_id()

    with open(EMPLOYEE_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([employee_id, first_name, last_name, position, salary, department, programming_language])
        print("Processing....")
        sleep(2)
        print()
    print(f"Employee {first_name} {last_name} added successfully!\n")


def view_employees():
    
    with open(EMPLOYEE_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)  
        print("ID  | First Name | Last Name | Position | Salary | Department | Programming Language")
        print("------------------------------------------------------------------------------------")
        for row in reader:
            if row and len(row) == 7:  
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]}")
        print("\n")


def edit_employee():
    
    employee_id = input("Enter the Employee ID to edit: ")
    found = False
    updated_data = []
    
    with open(EMPLOYEE_FILE, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  
        updated_data.append(header)  
        
        for row in reader:
            if row[0] == employee_id:
                found = True
                print(f"Editing Employee {row[1]} {row[2]}:")
                row[1] = input(f"New First Name ({row[1]}): ") or row[1]
                row[2] = input(f"New Last Name ({row[2]}): ") or row[2]
                row[3] = input(f"New Position ({row[3]}): ") or row[3]
                row[4] = input(f"New Salary ({row[4]}): ") or row[4]
                row[5] = input(f"New Department ({row[5]}): ") or row[5]
                row[6] = input(f"New Programming Language ({row[6]}): ") or row[6]
            updated_data.append(row)
    
    if not found:
        print(f"Employee with ID {employee_id} not found.\n")
        return
    
    with open(EMPLOYEE_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_data)
    print("Processing...")
    sleep(2)
    print()
    print(f"Employee {employee_id} updated successfully!\n")


def delete_employee():
    
    employee_id = input("Enter the Employee ID to delete: ")
    found = False
    updated_data = []
    
    with open(EMPLOYEE_FILE, 'r') as file:
        reader = csv.reader(file)
        header = next(reader) 
        updated_data.append(header) 
        
        for row in reader:
            if row[0] != employee_id:
                updated_data.append(row)
            else:
                found = True
    
    if not found:
        print(f"Employee with ID {employee_id} not found.\n")
        return

    with open(EMPLOYEE_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_data)
    print(f"Employee {employee_id} deleted successfully!\n")


# Main menu
def main_menu():
    """Main menu to navigate through employee management options."""
    while True:
        print("Employee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Edit Employee")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            edit_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("Exiting the program. Goodbye! :D")
            break
        else:
            print("Invalid choice :(. Please select between 1 and 5.\n")


# Initialize file and start the program
initialize_employee_file()
main_menu()
