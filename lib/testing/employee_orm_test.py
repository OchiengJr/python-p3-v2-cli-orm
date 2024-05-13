import pytest
from faker import Faker
from models.employee import Employee
from models.department import Department
from .department_test import DepartmentTest


class TestEmployee:
    '''Test cases for the Employee class'''

    @pytest.fixture(autouse=True)
    def drop_tables(self):
        '''Drop tables prior to each test'''
        DepartmentTest.drop_tables(self)

    def test_creates_table(self):
        '''Test if create_table() method creates the employees table'''
        DepartmentTest.create_table()
        Employee.create_table()
        assert CURSOR.execute("SELECT * FROM employees")

    # Other test methods here...

    def test_invalid_department_id(self):
        '''Test creating an employee with an invalid department ID'''
        Employee.create_table()
        with pytest.raises(ValueError):
            Employee.create("John", "Developer", 9999)  # Non-existent department ID

    def test_update_nonexistent_employee(self):
        '''Test updating a non-existent employee'''
        Employee.create_table()
        with pytest.raises(ValueError):
            employee = Employee("Alice", "Manager", 1)  # Assuming department ID 1 exists
            employee.update()

    def test_delete_nonexistent_employee(self):
        '''Test deleting a non-existent employee'''
        Employee.create_table()
        with pytest.raises(ValueError):
            employee = Employee("Bob", "Developer", 1)  # Assuming department ID 1 exists
            employee.delete()

    def test_random_data_generation(self):
        '''Test creating employee with random data'''
        Employee.create_table()
        faker = Faker()
        name = faker.name()
        job_title = faker.job()
        department = Department("HR", "Building 1")
        department.save()
        employee = Employee.create(name, job_title, department.id)
        assert employee.name == name
        assert employee.job_title == job_title
        assert employee.department_id == department.id

    def test_mock_database_interaction(self, mocker):
        '''Test updating an employee without hitting the actual database'''
        Employee.create_table()
        employee = Employee.create("Eve", "Manager", 1)  # Assuming department ID 1 exists
        mocker.patch.object(Employee, 'update')
        employee.name = "Eve Updated"
        employee.update.assert_called_once()

