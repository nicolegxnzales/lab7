# Program Name: Lab7.py
# Course: IT1114/Section XXX
# Student Name: Nicole Gonzales
# Assignment Number: Lab#7
# Due Date: 10/11/ 2024
# Purpose: For this lab you will modify your class from Lab 6. Add the following attributes/methods to your
# worker class.
class Worker:

    def __init__ (self):
        # attributes
        self.EmployeeNumber = None
        self.OfficeNumber = None
        self.Name = ""
        self.BirthDate =(None,None,None)
        self.totalHoursWorked = 0
        self.totalOvertimeHours = 0
        self.hourlySalary = 0
        self.OvertimeHourlySalary = 0


    #getter and setter for employee number
    def get_employee_number(self):
        return self.EmployeeNumber


    def set_employee_number(self,x):
        self.EmployeeNumber = x


    #getter and setter for office number
    def get_office_number(self):
        return self.OfficeNumber

    def set_office_number(self,x):
        if 100 <= x <= 500:
            self.OfficeNumber = x
            return True
        return False
    #getter and setter for name
    def get_name(self):
        return self.Name


    def set_name(self,x):
        self.Name = x

    #getter and setter fir birthdate
    def get_birthdate(self):
        return self.BirthDate

    def set_birthdate(self,m,d,y):
        if 1 <= m <= 12 and 1 <= d <= 31:
            self.BirthDate = (m,d,y)

            return True
        return False

    #getter and setter for hours worked
    def get_hours_worked(self):
        return self.totalHoursWorked

    def add_hours(self,x):
        if x > 9:
            self.totalHoursWorked += 9
            self.totalOvertimeHours += x - 9
        else:
            self.totalHoursWorked += x

    #getter for overtime hours
    def get_hours_overtime(self):
        return self.totalOvertimeHours

    #getters and setters for hourly salary lab 7
    def get_hourly_salary(self):
        return self.hourlySalary


    def set_hourly_salary(self,x):
        self.hourlySalary = x
        if x<0 :
            return False
        return True

    #getter and setter for overtime salary lab 7
    def get_overtime_salary(self):
        return self.OvertimeHourlySalary


    def set_overtime_salary(self,x):
        self.OvertimeHourlySalary =x
        if x<0:
            return False
        return True


    #getter for pay
    def get_pay(self):
        return (self.totalHoursWorked * self.hourlySalary)+(self.totalOvertimeHours* self.OvertimeHourlySalary)