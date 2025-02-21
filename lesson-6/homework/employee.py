import os


class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            open(self.FILE_NAME, 'w').close()

    def add_employee(self, employee):
        with open(self.FILE_NAME, 'a') as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        with open(self.FILE_NAME, 'r') as file:
            employees = file.readlines()
        if not employees:
            print("No records found.")
        else:
            for emp in employees:
                print(emp.strip())

    def search_employee(self, employee_id):
        with open(self.FILE_NAME, 'r') as file:
            employees = file.readlines()
        for emp in employees:
            data = emp.strip().split(', ')
            if data[0] == employee_id:
                print("Employee Found:", emp.strip())
                return
        print("Employee not found.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        updated = False
        with open(self.FILE_NAME, 'r') as file:
            employees = file.readlines()
        with open(self.FILE_NAME, 'w') as file:
            for emp in employees:
                data = emp.strip().split(', ')
                if data[0] == employee_id:
                    if name: data[1] = name
                    if position: data[2] = position
                    if salary: data[3] = salary
                    file.write(", ".join(data) + "\n")
                    updated = True
                else:
                    file.write(emp)
        if updated:
            print("Employee updated successfully!")
        else:
            print("Employee not found.")

    def delete_employee(self, employee_id):
        deleted = False
        with open(self.FILE_NAME, 'r') as file:
            employees = file.readlines()
        with open(self.FILE_NAME, 'w') as file:
            for emp in employees:
                data = emp.strip().split(', ')
                if data[0] == employee_id:
                    deleted = True
                else:
                    file.write(emp)
        if deleted:
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    def run(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                self.add_employee(Employee(emp_id, name, position, salary))
            elif choice == '2':
                self.view_all_employees()
            elif choice == '3':
                emp_id = input("Enter Employee ID: ")
                self.search_employee(emp_id)
            elif choice == '4':
                emp_id = input("Enter Employee ID: ")
                name = input("Enter new Name (leave blank to keep unchanged): ") or None
                position = input("Enter new Position (leave blank to keep unchanged): ") or None
                salary = input("Enter new Salary (leave blank to keep unchanged): ") or None
                self.update_employee(emp_id, name, position, salary)
            elif choice == '5':
                emp_id = input("Enter Employee ID: ")
                self.delete_employee(emp_id)
            elif choice == '6':
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.run()
