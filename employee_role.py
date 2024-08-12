from faker import Faker
import random

fake = Faker()

# Open a file to write the SQL commands
with open('insert_employee_role.sql', 'w') as file:
    for role_id in range(1, 20001):
        employee_id = role_id  # Sequential employee_id from 1 to 20000
        role_description = fake.job()  # Generate a random job title as role description
        change_datetime = 'NOW()'  # Use NOW() to get the current datetime

        # Format the SQL INSERT command
        sql = f"INSERT INTO employee_role (role_id, employee_id, role_description, change_datetime) VALUES ({role_id}, {employee_id}, '{role_description}', {change_datetime});\n"
        # Write the command to the file
        file.write(sql)
