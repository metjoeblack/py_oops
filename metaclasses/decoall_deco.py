"""
Apply any decorator to all methods of a class, with a decorator
"""

import time
from types import FunctionType
from metaclassess.decorators import timer, tester


def decorate_all(decorator):
    def deco_decorator(a_class):
        for attr, attr_value in a_class.__dict__.items():
            if type(attr_value) is FunctionType and not attr.startswith('__'):
                setattr(a_class, attr, decorator(attr_value))  # not __dict__
                # Wrong: a_class.__dict__[attr] = decorator(attr_value)
        return a_class
    return deco_decorator


@decorate_all(timer(label="==>", want_trace=True))
class Person:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def give_raise(self, percent):
        time.sleep(0.5)
        self.pay *= (1 + percent)

    def get_last_name(self):
        time.sleep(0.5)
        return self.name.split()[-1]


if __name__ == '__main__':
    tester(Person)
