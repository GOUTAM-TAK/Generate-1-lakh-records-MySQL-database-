from faker import Faker
import random

fake = Faker()

def generate_employees_inserts(n):
    inserts = []
    for _ in range(n):
        employee_id = _
        first_name = fake.first_name()
        last_name = fake.last_name()
        department_id = random.randint(1, 100)  # Adjust based on your departments table
        email = fake.email()
        phone = fake.phone_number()
        hire_date = fake.date()
        change_datetime = fake.date_time_this_year()

        insert_statement = f"INSERT INTO employees (employee_id, first_name, last_name, department_id, email, phone, hire_date, change_datetime) VALUES ({employee_id}, '{first_name}', '{last_name}', {department_id}, '{email}', '{phone}', '{hire_date}', '{change_datetime}');"
        inserts.append(insert_statement)
    return inserts

# Generate 20,000 inserts
inserts = generate_employees_inserts(20000)

# Write to a file
with open('employees_inserts.sql', 'w') as f:
    f.write('\n'.join(inserts))
