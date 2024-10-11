# lab7
# Worker Class - Lab 7

## Project Overview
This project is part of Lab 7 of the IT1114 course. The goal is to extend the existing `Worker` class (from Lab 6) to include additional attributes and methods that calculate the salary for regular and overtime hours worked by an office worker.

## Features
The `Worker` class now includes:
- Employee number, office number, name, and birthdate.
- Tracking of total hours worked and overtime hours.
- **New attributes** for hourly salary and overtime salary.
- Methods to set and retrieve hourly salary and overtime salary.
- Method to calculate total pay based on regular and overtime hours worked.

## Methods Overview
- `__init__()` - Initializes the attributes for the worker.
- `get_employee_number()` / `set_employee_number(x)` - Get or set the employee number.
- `get_office_number()` / `set_office_number(x)` - Get or set the office number, validates office numbers between 100 and 500.
- `get_name()` / `set_name(x)` - Get or set the worker's name.
- `get_birthdate()` / `set_birthdate(m, d, y)` - Get or set the worker's birthdate. Ensures the day is between 1-31 and month between 1-12.
- `get_hours_worked()` - Returns the total hours worked.
- `add_hours(x)` - Adds hours worked. If hours exceed 9, the extra time is considered overtime.
- `get_hours_overtime()` - Returns the number of overtime hours worked.

**New Methods**:
- `set_hourly_salary(x)` - Sets the hourly salary. Returns `False` if the salary is negative, otherwise `True`.
- `set_overtime_salary(x)` - Sets the overtime salary. Returns `False` if the salary is negative, otherwise `True`.
- `get_hourly_salary()` - Returns the hourly salary.
- `get_overtime_salary()` - Returns the overtime salary.
- `get_pay()` - Calculates and returns the worker's total pay based on regular and overtime hours worked.

## Usage Example
Here is how you can use the `Worker` class:
```python
worker = Worker()
worker.set_employee_number(12345)
worker.set_office_number(250)
worker.set_name("John Doe")
worker.set_birthdate(5, 15, 1990)
worker.add_hours(12)  # Adds 9 regular hours, 3 overtime hours
worker.set_hourly_salary(20)
worker.set_overtime_salary(30)

print(worker.get_employee_number())  # Output: 12345
print(worker.get_pay())              # Output: Total pay based on hours and overtime
