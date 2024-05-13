#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.department import Department
from models.employee import Employee

def seed_database():
    try:
        # Drop existing tables
        Employee.drop_table()
        Department.drop_table()

        # Create tables
        Department.create_table()
        Employee.create_table()

        # Create seed data
        payroll = Department.create("Payroll", "Building A, 5th Floor")
        human_resources = Department.create(
            "Human Resources", "Building C, East Wing")
        Employee.create("Amir", "Accountant", payroll.id)
        Employee.create("Bola", "Manager", payroll.id)
        Employee.create("Charlie", "Manager", human_resources.id)
        Employee.create("Dani", "Benefits Coordinator", human_resources.id)
        Employee.create("Hao", "New Hires Coordinator", human_resources.id)

        print("Database seeded successfully.")

    except Exception as e:
        print(f"Error while seeding database: {str(e)}")
        CONN.rollback()

    finally:
        CURSOR.close()
        CONN.close()

if __name__ == "__main__":
    seed_database()
