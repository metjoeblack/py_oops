"""Extend a class with metaclass"""

from pprint import pprint


def triple(obj):
    return obj.value * 3


def concat(obj):
    return obj.value + 'Code!'


class ExtenderMeta(type):
    def __new__(cls, classname, supers, classdict):
        classdict['triple'] = triple
        classdict['concat'] = concat
        # pprint(classdict)
        return type.__new__(cls, classname, supers, classdict)


class ClientOne(metaclass=ExtenderMeta):
    def __init__(self, value):
        self.value = value

    def double(self):
        return self.value * 2


class ClientTwo(metaclass=ExtenderMeta):
    value = "grok"


def main():
    x = ClientOne('Hack')
    print(x.value, x.triple(), x.double(), x.concat(), sep='\n')
    pprint(ClientOne.__dict__)
    print(x.__dict__)

    y = ClientTwo()
    print(y.value, y.triple(), y.concat(), sep='\n')
    pprint(ClientTwo.__dict__)
    print(y.__dict__)


if __name__ == '__main__':
    main()