import pytest
from models.department import Department


class TestDepartmentProperties:
    '''Test cases for Department class properties'''

    @pytest.fixture
    def department(self):
        '''Create a Department instance'''
        return Department("Payroll", "Building A, 5th Floor")

    def test_valid_name_location(self, department):
        '''Name and location should be valid non-empty strings'''
        assert department.name == "Payroll"
        assert department.location == "Building A, 5th Floor"

    def test_name_is_string(self, department):
        '''Name property should only accept strings'''
        with pytest.raises(ValueError):
            department.name = 7

    def test_name_string_length(self, department):
        '''Name property length should be greater than 0'''
        with pytest.raises(ValueError):
            department.name = ''

    def test_location_is_string(self, department):
        '''Location property should only accept strings'''
        with pytest.raises(ValueError):
            department.location = True

    def test_location_string_length(self, department):
        '''Location property length should be greater than 0'''
        with pytest.raises(ValueError):
            department.location = ''
