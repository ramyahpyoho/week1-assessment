
# Task 1: Python Core, OOP and Errors

# 1. Function with *args and **kwargs
def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)

    if "cap" in options:
        result = min(result, options["cap"])

    return result


print("Bonus:", bonus(50000, 0.1, 500, 1000, cap=6000))


# 2. Custom exception
class InvalidSalaryError(Exception):
    pass


# 3. Employee class
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(
                f"Invalid salary: {salary}"
            )

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"{self.name}: {self.salary}"


# 4. Manager inheritance
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"{self.name}: {self.salary}, "
            f"Team size: {self.team_size}"
        )


employee = Employee("Rahul", 60000)
manager = Manager("Priya", 80000, 5)

print("Annual salary:", employee.annual_salary())
print("Manager:", manager.get_details())


# 5. Exception handling
try:
    invalid_employee = Employee("Test", -500)

except InvalidSalaryError as error:
    print("Error:", error)

finally:
    print("Transaction finished")





import csv

# Read employee data from CSV
with open("task1/employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

# Convert salary values from string to integer
for emp in employees:
    emp["salary"] = int(emp["salary"])

# 6. List comprehension: employees earning above 50000
high_salary_names = [
    emp["name"] for emp in employees
    if emp["salary"] > 50000
]
print("Employees earning above 50000:", high_salary_names)

# 7. Map and lambda: give everyone a 10% raise
raised_salaries = list(
    map(lambda emp: emp["salary"] * 1.10, employees)
)
print("Salaries after 10% raise:", raised_salaries)

# 8. Filter: employees from Chennai
chennai_employees = list(
    filter(lambda emp: emp["city"] == "Chennai", employees)
)
print("Chennai employees:", [
    emp["name"] for emp in chennai_employees
])

# 9. Loop with continue and break
print("Loop output:")

for emp in employees:
    if emp["salary"] == 0:
        continue

    print(emp["name"], emp["salary"])

    if emp["salary"] > 85000:
        break