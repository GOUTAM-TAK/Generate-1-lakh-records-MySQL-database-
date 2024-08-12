from faker import Faker
import random

fake = Faker()

# Open a file to write the SQL commands
with open('insert_projects.sql', 'w') as file:
    for i in range(1, 20001):
        project_id = i
        project_name = fake.unique.company()  # Generate a unique project name
        start_date = fake.date_this_decade(before_today=True, after_today=False)  # Random start date within the last decade
        end_date = fake.date_between(start_date=start_date, end_date='+2y')  # End date up to 2 years after the start date
        department_id = random.randint(1, 100)  # Department ID between 1 and 100
        change_datetime = 'NOW()'  # Use NOW() to get the current datetime

        # Format the SQL INSERT command
        sql = f"INSERT INTO projects (project_id, project_name, start_date, end_date, department_id, change_datetime) VALUES ({project_id}, '{project_name}', '{start_date}', '{end_date}', {department_id}, {change_datetime});\n"
        # Write the command to the file
        file.write(sql)
