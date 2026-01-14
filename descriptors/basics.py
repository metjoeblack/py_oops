
class Descriptor:
    def __get__(self, instance, owner):
        print(self, instance, owner, sep=', ')
        return 'I am a hypothetical attr here.'


class Subject:
    attr = Descriptor()


def func_1():
    x = Subject()
    print(x.attr)
    print(getattr(x, 'attr'))
    print(Subject.attr)


class ReadOnlyDescriptor:
    """
    To make a descriptor-based attribute read-only, catch the
    assignment in the descriptor class and raise an exception
    to prevent attribute assignment.
    """
    def __get__(self, instance, owner):
        print(self, instance, owner, sep=', ')

    def __set__(self, instance, value):
        raise AttributeError(f"can't set attribute")


class Desc:
    a = ReadOnlyDescriptor()


def func_2():
    x = Desc()
    print(x.a)
    x.a = 99


class Person:
    """
    When a descriptor class is not useful outside the client class,
    it's perfectly reasonable to embed the descriptor's definition
    inside its client syntactically.
    """
    class NameDescriptor:
        """It's a name descriptor docs"""
        def __get__(self, instance, owner):
            print('fetch ...')
            return getattr(instance, '_name')

        def __set__(self, instance, value):
            print('change ...')
            instance._name = value

        def __delete__(self, instance):
            print('delete ...')
            delattr(instance, '_name')

    name = NameDescriptor()

    def __init__(self, name, age):
        self._name = name
        self.age = age

    @staticmethod
    def main():
        sue = Person('Sue Jones', 20)
        print(sue.name)
        sue.age = 21
        sue.name = 'Susan Jones'
        print(Person.NameDescriptor.__doc__)
        del sue.name


class DescSquare:
    def __init__(self, start):
        self.value = start

    def __get__(self, instance, owner):
        return self.value ** 2

    def __set__(self, instance, value):
        self.value = value


class Client1:
    x = DescSquare(2)
    y = DescSquare(3)


class Client2:
    x = DescSquare(4)
    z = DescSquare(5)


def func_3():
    c1 = Client1()
    print(c1.x)
    print(c1.y)
    print(c1.__dict__)
    c1.x = 100
    print(c1.__dict__)
    print(c1.x)

    c2 = Client2()
    print(c2.x)
    print(c2.z)
    print(c2.__dict__)


if __name__ == '__main__':
    # func_2()
    # Person.main()
    func_3()
    pass