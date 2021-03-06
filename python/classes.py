# why use classes ( OOP ) : allow us tp group data and funtions and build on top of them with methods
import unittest


class Employee:

    RAISE_AMOUNT = 1.04
    num_employes = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_employes += 1  # we can use self but class name is better here

    def fullname(self):
        return "this is: {} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.RAISE_AMOUNT)

    @classmethod  # create methods to interacate with the constants
    def set_raise_amt(
        cls, amount
    ):  # cls remplace name of the calsse here its: Employee
        cls.RAISE_AMOUNT = amount

    @classmethod
    def from_string(cls, emp_str):  # cls remplace name of the calsse here its: Employee
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)


emp1 = Employee("Aghiles", "Schafer", 40000)
emp2 = Employee("moh", "lbilot", 100000)


Employee.set_raise_amt(1.05)
print("upgrade employe 1: ", emp1.RAISE_AMOUNT)
print("upgrade employe 2: ", emp2.RAISE_AMOUNT)
print("num of employee: ", Employee.num_employes)

emp3 = Employee.from_string("aghiles-aitlounis-100000")

print("test: ", emp3.pay, emp3.first)
