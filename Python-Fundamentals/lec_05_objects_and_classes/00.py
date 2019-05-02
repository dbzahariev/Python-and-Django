class Employee:
    rise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_rise(self):
        self.pay = float(self.pay * self.rise_amount)


emp_1 = Employee('Correy', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.rise_amount)
print(emp_1.rise_amount)
print(emp_2.rise_amount)
