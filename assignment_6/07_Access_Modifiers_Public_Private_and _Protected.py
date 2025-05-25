class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            #public
        self._salary = salary       #protected
        self.__ssn = ssn            #private
    
    def salary(self):
        return self._salary  #acessing sslary (protected)

    def ssn(self):
        return self.__ssn   #accessing ssn (private)

    
emp = Employee("hayyan", 1400, "abcde")

print(f"Emloyee name: {emp.name}")
print(f"Employee Salary:{emp.salary()}")
print(f"Employee ssn: {emp.ssn()}")