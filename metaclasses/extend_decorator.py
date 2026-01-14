"""Extend a class with a decorator"""

from pprint import pprint


def triple(obj):
    return obj.value * 3


def concat(obj):
    return obj.value + 'Code!'


def extender(a_class):
    a_class.triple = triple
    a_class.concat = concat
    return a_class


@extender
class ClientOne:
    def __init__(self, value):
        self.value = value

    def double(self):
        return self.value * 2


@extender
class ClientTwo:
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