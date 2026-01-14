"""
Record and process information about people.
Run this file directly to test its classes.
"""
# from classtools import AttrsDisplay
from listinstance import ListInstance


class Person(ListInstance):
    """Create and process person records."""
    def __init__(self, name, job=None, paycheck=0):
        self.name = name
        self.job = job
        self.paycheck = paycheck

    def get_last_name(self):
        return self.name.split()[-1]

    def give_pay_rise(self, percent):
        self.paycheck = int(self.paycheck * (1 + percent))


class Manager(Person):
    """A customized Person with special requirements."""
    def __init__(self, name, paycheck=0):
        Person.__init__(self, name, "mgr", paycheck)
    
    def give_pay_rise(self, percent, bonus=.10):
        Person.give_pay_rise(self, percent + bonus)


class ManagerComposite:
    def __init__(self, name, paycheck):
        self.person = Person(name, "mgr", paycheck)

    def give_pay_rise(self, percent, bonus=.10):
        self.person.give_pay_rise(percent + bonus)

    def __repr__(self):
        attrs = (f"{k}={v!r}" for k, v in vars(self.person).items())
        return (
            f"{self.__class__.__name__}"
            f"({', '.join(attrs)})"
        )

    def __getattr__(self, attr):
        return getattr(self.person, attr)


if __name__ == '__main__':
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", paycheck=100_000)
    pat = Manager("Pat Jones", paycheck=50_000)
    jane = ManagerComposite("Jane Alan", paycheck=100_000)
    for obj in (bob, sue, pat, jane):
        obj.give_pay_rise(.10)
        print(obj)
    pass