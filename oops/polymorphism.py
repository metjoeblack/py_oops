

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compute_salary(self):
        pass

    def give_raise(self):
        pass

    def promote(self):
        pass

    def retire(self):
        pass


class Engineer(Employee):
    def compute_salary(self):
        pass


if __name__ == '__main__':
    sue = Employee("Sue", 25)
    bob = Employee("Bob", 25)
    pat = Engineer("Pat", 25)

    employees = [sue, bob, pat]
    for employee in employees:
        print(employee.compute_salary())