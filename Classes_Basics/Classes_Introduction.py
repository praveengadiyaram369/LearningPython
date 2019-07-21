############## Introduction to classes to Instances ##############
import datetime

class Employee:
    raise_pay_amount = 0.12
    employee_count = 0

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        Employee.employee_count += 1

    def print_full_name(self):
        print(f'{self.firstName} {self.lastName} and with pay of {self.pay}')

    def raise_pay(self):
        self.pay = int(self.pay * self.raise_pay_amount)

    @classmethod
    def set_raise_pay_amout(cls,pay):
        Employee.raise_pay_amount = pay

    @classmethod
    def from_string_to_object(cls, emp_str):
        firstName, lastName, pay = emp_str.split('-')
        return cls(firstName, lastName, pay)

    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 0:
            return False
        else:
            return True

class Developer(Employee):
    pass



emp_1 = Employee('Praveen', 'Gadiyaram', 1000)
emp_2 = Employee('Rahul', 'Dravid', 10000)

print(emp_1)
emp_1.print_full_name()
emp_2.print_full_name()
#Employee.printFullName(emp_2)
#Employee.printFullName(emp_1)
print(Employee.__dict__)

emp_1.raise_pay()
emp_2.raise_pay_amount = 0.23
emp_2.raise_pay()
print(emp_1.__dict__)
print(emp_2.__dict__)

print(emp_1.pay)
print(emp_2.pay)
print(Employee.employee_count)

Employee.set_raise_pay_amout(4.3)
print(Employee.raise_pay_amount)


emp_str_1 = 'kristen-stewart-2000'
emp_str_2 = 'gal-gadot-5000'

emp_obj_1 = Employee.from_string_to_object(emp_str_1)
emp_obj_2 = Employee.from_string_to_object(emp_str_2)

emp_obj_1.print_full_name()
emp_obj_2.print_full_name()


my_date = datetime.date(2018, 8, 25)
print(Employee.is_weekday(my_date))


##print(help(Developer))
dev_1 = Developer('Scarlet', 'Johnson', 7000)
dev_2 = Developer('Emilia', 'Clark', 6000)

dev_1.print_full_name()
dev_2.print_full_name()