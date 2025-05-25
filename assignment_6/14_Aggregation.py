class Employee:
    def __init__(self, name):
        self.name = name

    def show_employee(self):
        print(f"employee: {self.name}")
        pass

class Department:
    def __init__(self, employee):
        self.employee = employee

    def show_employe(self):
        self.employee.show_employee()

emp1 = Employee("hayyan")
dept1  = Department(emp1)
dept1.show_employe()

del dept1
emp1.show_employee()