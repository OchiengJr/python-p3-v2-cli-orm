import pytest
from models.department import Department
from models.employee import Employee

@pytest.fixture(autouse=True)
def drop_tables():
    '''Drop tables prior to each test.'''
    Employee.drop_table()
    Department.drop_table()
    Department.all = {}


class TestDepartment:
    '''Test cases for Department class'''

    @staticmethod
    def setup_method():
        Department.create_table()

    def teardown_method(self):
        Department.drop_table()

    def test_create_table(self):
        '''Test create_table method'''
        Department.create_table()
        assert Department.get_all() == []

    def test_drop_table(self):
        '''Test drop_table method'''
        Department.drop_table()
        assert Department.get_all() == []

    @pytest.mark.parametrize("name, location", [
        ("Payroll", "Building A, 5th Floor"),
        ("Human Resources", "Building C, East Wing")
    ])
    def test_create_department(self, name, location):
        '''Test create method'''
        department = Department.create(name, location)
        assert Department.find_by_id(department.id) == department

    def test_update_department(self):
        '''Test update method'''
        department = Department.create("Marketing", "Building B, 3rd Floor")
        department.name = "Sales and Marketing"
        department.location = "Building B, 4th Floor"
        department.update()
        assert Department.find_by_id(department.id) == department

    def test_delete_department(self):
        '''Test delete method'''
        department = Department.create(
            "Sales and Marketing", "Building B, 4th Floor")
        department.delete()
        assert Department.find_by_id(department.id) is None

    def test_find_by_id(self):
        '''Test find_by_id method'''
        department = Department.create("Finance", "Building D, 1st Floor")
        assert Department.find_by_id(department.id) == department

    def test_find_by_name(self):
        '''Test find_by_name method'''
        department = Department.create("Finance", "Building D, 1st Floor")
        assert Department.find_by_name("Finance") == department

    def test_employees(self):
        '''Test employees method'''
        department = Department.create(
            "Sales", "Building E, 2nd Floor")
        employee1 = Employee.create("John", "Sales Representative", department.id)
        employee2 = Employee.create("Alice", "Sales Manager", department.id)
        assert department.employees() == [employee1, employee2]
