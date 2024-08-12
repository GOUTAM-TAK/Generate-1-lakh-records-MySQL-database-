from faker import Faker
import random

fake = Faker()

# Open a file to write the SQL commands
with open('insert_departments.sql', 'w') as file:
    for i in range(1, 101):
        department_name = fake.unique.company()  # Generate a unique department name
        location = fake.city()  # Generate a random location
        # Format the SQL INSERT command
        sql = f"INSERT INTO departments (department_id, department_name, location, change_datetime) VALUES ({i}, '{department_name}', '{location}', NOW());\n"
        # Write the command to the file
        file.write(sql)
