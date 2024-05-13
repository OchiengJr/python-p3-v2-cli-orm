#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.department import Department
from models.employee import Employee
import ipdb


def reset_database():
    try:
        # Drop existing tables
        Employee.drop_table()
        Department.drop_table()
    except Exception as e:
        print(f"Error dropping tables: {e}")
        # Log the error if needed

    try:
        # Create new tables
        Department.create_table()
        Employee.create_table()
    except Exception as e:
        print(f"Error creating tables: {e}")
        # Log the error if needed

    # Seed data
    try:
        payroll = Department.create("Payroll", "Building A, 5th Floor")
        human_resources = Department.create(
            "Human Resources", "Building C, East Wing")
        Employee.create("Amir", "Accountant", payroll.id)
        Employee.create("Bola", "Manager", payroll.id)
        Employee.create("Charlie", "Manager", human_resources.id)
        Employee.create("Dani", "Benefits Coordinator", human_resources.id)
        Employee.create("Hao", "New Hires Coordinator", human_resources.id)
    except Exception as e:
        print(f"Error seeding data: {e}")
        # Log the error if needed


reset_database()
ipdb.set_trace()  # Remember to remove this before deploying to production
