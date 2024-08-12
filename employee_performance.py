from faker import Faker
import random

fake = Faker()

# Open a file to write the SQL commands
with open('insert_employee_performance.sql', 'w') as file:
    for i in range(1, 20001):
        performance_id = i
        employee_id = random.randint(1, 20000)  # Employee ID between 1 and 20000
        project_id = random.randint(1, 20000)   # Project ID between 1 and 20000 (assuming valid IDs in projects table)
        score = random.randint(1, 100)          # Score between 1 and 100
        comment = 'good' if score > 50 else 'bad'  # Comment based on the score
        change_datetime = 'NOW()'  # Use NOW() to get the current datetime

        # Format the SQL INSERT command
        sql = f"INSERT INTO employee_performance (performance_id, employee_id, project_id, score, comment, change_datetime) VALUES ({performance_id}, {employee_id}, {project_id}, {score}, '{comment}', {change_datetime});\n"
        # Write the command to the file
        file.write(sql)
