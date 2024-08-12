from faker import Faker
import random
import pandas as pd

fake = Faker()

# Open a file to write the SQL commands
with open('insert_employee_salaries.sql', 'w') as file:
    for i in range(1, 20001):
        salary_id = i
        employee_id = random.randint(1, 20000)  # Adjust this range based on the actual range of employee_ids
        salary = round(random.uniform(30000, 120000), 2)  # Generate a random salary between $30,000 and $120,000
        start_date = fake.date_this_decade(before_today=True, after_today=False)  # Random date within this decade
        end_date = fake.date_between(start_date=start_date, end_date='+1y')  # End date 1 year after the start date
        change_datetime = 'NOW()'  # Use NOW() to get the current datetime

        # Format the SQL INSERT command
        sql = f"INSERT INTO employee_salaries (salary_id, employee_id, salary, start_date, end_date, change_datetime) VALUES ({salary_id}, {employee_id}, {salary}, '{start_date}', '{end_date}', {change_datetime});\n"
        # Write the command to the file
        file.write(sql)
