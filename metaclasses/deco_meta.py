
import time
from types import FunctionType
from metaclassess.decorators import timer, tester


def decorate_all(decorator):
    class MetaDecorate(type):
        def __new__(cls, classname, supers, classdict):
            # print(classdict)
            for attr, attr_value in classdict.items():
                if type(attr_value) is FunctionType and not attr.startswith('__'):
                    classdict[attr] = decorator(attr_value)
            return type.__new__(cls, classname, supers, classdict)
    return MetaDecorate


class Person(metaclass=decorate_all(timer(label="==>"))):
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def give_raise(self, percent):
        time.sleep(1)
        self.pay *= (1 + percent)

    def get_last_name(self):
        time.sleep(2)
        return self.name.split()[-1]


if __name__ == '__main__':
    tester(Person)
