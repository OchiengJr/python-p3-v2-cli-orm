from models.department import Department
from models.employee import Employee
import pytest


@pytest.fixture(scope='module')
def setup_database():
    '''Set up the database tables'''
    Employee.drop_table()
    Department.drop_table()
    Employee.create_table()
    Department.create_table()


class TestEmployeeProperties:
    '''Test cases for the properties of the Employee class'''

    @pytest.fixture(autouse=True)
    def reset_db(self, setup_database):
        '''Reset the database before each test'''
        Department.all = {}
        Employee.all = {}

    def test_name_job_title_valid(self):
        '''Validate name and job title properties'''
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Lee", "Manager", department.id)  # No exception

    @pytest.mark.parametrize("invalid_value", [7, '', None])
    def test_name_is_string_and_non_empty(self, invalid_value):
        '''Validate name property is a non-empty string'''
        department = Department.create("Payroll", "Building A, 5th Floor")
        with pytest.raises(ValueError):
            employee = Employee.create("Lee", "Manager", department.id)
            employee.name = invalid_value

    @pytest.mark.parametrize("invalid_value", [7, '', None])
    def test_job_title_is_string_and_non_empty(self, invalid_value):
        '''Validate job title property is a non-empty string'''
        department = Department.create("Payroll", "Building A, 5th Floor")
        with pytest.raises(ValueError):
            employee = Employee.create("Lee", "Manager", department.id)
            employee.job_title = invalid_value

    def test_department_property_valid(self):
        '''Validate department property is set correctly'''
        department = Department.create("Payroll", "Building C, 3rd Floor")
        employee = Employee.create("Raha", "Accountant", department.id)  # No exception

    def test_invalid_department_id(self):
        '''Validate invalid department ID raises ValueError'''
        with pytest.raises(ValueError):
            Employee.create("Raha", "Accountant", 7)  # Non-existent department ID

    def test_invalid_department_id_type(self):
        '''Validate department ID must be an integer'''
        with pytest.raises(ValueError):
            Employee.create("Raha", "Accountant", "abc")  # Invalid department ID type
