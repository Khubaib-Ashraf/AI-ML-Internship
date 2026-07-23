# Task 2: Create an Employee class with salary calculation

class Employee:
    def __init__(self, name, employee_id, base_salary, hours_worked):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary
        self.hours_worked = hours_worked

    def calculate_salary(self):
        salary = self.base_salary

        if self.hours_worked > 160:
            extra_hours = self.hours_worked - 160
            salary = salary + (extra_hours * 30)

        return salary

    def display_info(self):
        return f"Name: {self.name}\nID: {self.employee_id}\nSalary: ${self.calculate_salary()}"


# Main Program
employee1 = Employee("Ali Hain", "EMP001", 3000, 180)
employee2 = Employee("Zain", "EMP002", 3500, 130)
employee3 = Employee("Daniyal", "EMP003", 3100, 190)
employee4 = Employee("Akbar Ali", "EMP004", 3000, 170)
print(employee1.display_info())
print(employee2.display_info())
print(employee3.display_info())
print(employee4.display_info())
