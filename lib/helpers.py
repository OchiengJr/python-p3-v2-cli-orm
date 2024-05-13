from models.department import Department
from models.employee import Employee

def exit_program():
    print("Goodbye!")
    exit()

# Department Functions

def list_departments():
    departments = Department.get_all()
    if departments:
        print("List of Departments:")
        for department in departments:
            print(f"ID: {department.id}, Name: {department.name}, Location: {department.location}")
    else:
        print("No departments found.")

def find_department_by_name():
    name = input("Enter department name: ")
    department = Department.find_by_name(name)
    if department:
        print(f"Department found - ID: {department.id}, Name: {department.name}, Location: {department.location}")
    else:
        print("Department not found.")

def find_department_by_id():
    id = input("Enter department ID: ")
    department = Department.find_by_id(id)
    if department:
        print(f"Department found - ID: {department.id}, Name: {department.name}, Location: {department.location}")
    else:
        print("Department not found.")

def create_department():
    name = input("Enter department name: ")
    location = input("Enter department location: ")
    department = Department.create(name, location)
    if department:
        print(f"Department created - ID: {department.id}, Name: {department.name}, Location: {department.location}")
    else:
        print("Failed to create department.")

def update_department():
    id = input("Enter department ID to update: ")
    department = Department.find_by_id(id)
    if department:
        name = input("Enter new department name (leave blank to keep current): ")
        location = input("Enter new department location (leave blank to keep current): ")
        if name:
            department.name = name
        if location:
            department.location = location
        department.update()
        print("Department updated successfully.")
    else:
        print("Department not found.")

def delete_department():
    id = input("Enter department ID to delete: ")
    department = Department.find_by_id(id)
    if department:
        department.delete()
        print("Department deleted successfully.")
    else:
        print("Department not found.")

# Employee Functions

def list_employees():
    employees = Employee.get_all()
    if employees:
        print("List of Employees:")
        for employee in employees:
            print(f"ID: {employee.id}, Name: {employee.name}, Job Title: {employee.job_title}, Department ID: {employee.department_id}")
    else:
        print("No employees found.")

def find_employee_by_name():
    name = input("Enter employee name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(f"Employee found - ID: {employee.id}, Name: {employee.name}, Job Title: {employee.job_title}, Department ID: {employee.department_id}")
    else:
        print("Employee not found.")

def find_employee_by_id():
    id = input("Enter employee ID: ")
    employee = Employee.find_by_id(id)
    if employee:
        print(f"Employee found - ID: {employee.id}, Name: {employee.name}, Job Title: {employee.job_title}, Department ID: {employee.department_id}")
    else:
        print("Employee not found.")

def create_employee():
    name = input("Enter employee name: ")
    job_title = input("Enter employee job title: ")
    department_id = input("Enter department ID for employee: ")
    employee = Employee.create(name, job_title, department_id)
    if employee:
        print(f"Employee created - ID: {employee.id}, Name: {employee.name}, Job Title: {employee.job_title}, Department ID: {employee.department_id}")
    else:
        print("Failed to create employee.")

def update_employee():
    id = input("Enter employee ID to update: ")
    employee = Employee.find_by_id(id)
    if employee:
        name = input("Enter new employee name (leave blank to keep current): ")
        job_title = input("Enter new employee job title (leave blank to keep current): ")
        department_id = input("Enter new department ID for employee (leave blank to keep current): ")
        if name:
            employee.name = name
        if job_title:
            employee.job_title = job_title
        if department_id:
            employee.department_id = department_id
        employee.update()
        print("Employee updated successfully.")
    else:
        print("Employee not found.")

def delete_employee():
    id = input("Enter employee ID to delete: ")
    employee = Employee.find_by_id(id)
    if employee:
        employee.delete()
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")

def list_department_employees():
    department_id = input("Enter department ID: ")
    employees = Employee.find_by_department_id(department_id)
    if employees:
        print(f"Employees in Department {department_id}:")
        for employee in employees:
            print(f"ID: {employee.id}, Name: {employee.name}, Job Title: {employee.job_title}")
    else:
        print("No employees found in this department.")

# Main Menu

def main():
    while True:
        print("\nMain Menu:")
        print("1
