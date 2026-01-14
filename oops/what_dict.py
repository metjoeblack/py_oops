
class DemoClass:
    """This is a class docstring"""
    cls_attr = "This is a class attribute"

    def __init__(self):
        self.instance_attr = "This is a instance attribute"
        self.name = "Just a jok!"

    def method(self):
        return f"{self.__class__.__name__}'s method"


def show_object_dict(obj):
    for key, value in vars(obj).items():
        print(f"{key:<22}: {value}")


def demo1():
    show_object_dict(DemoClass)

    print("-" * 50)
    print(DemoClass.__dict__['__dict__'])

    print("-" * 50)
    demo_instance = DemoClass()
    print(demo_instance.__dict__)

    print(DemoClass.__dict__['method'].__dict__)



class Number:
    value = 42

    def __init__(self):
        self.value = 7


def demo2():
    show_object_dict(Number)
    num = Number()
    print(num.__dict__)
    print(Number.value, num.value)


def greet_name(name):
    print(f"Hello, {name}")


class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __str__(self):
        return "{name}, {age}, {job}".format(**self.__dict__)

    def __repr__(self):
        return "{cls}(name={name!r}, age={age!r}, job={job!r})".format(
            cls=type(self).__name__,
            **self.__dict__
        )

    def as_dict(self):
        return self.__dict__

    def as_tuple(self):
        return tuple(self.__dict__.values())

    @staticmethod
    def main():
        p = Person("John Nash", 24, "Developer")
        print(p)
        print(repr(p))
        print(p.as_dict())
        print(p.as_tuple())


if __name__ == '__main__':
    # demo1()
    # demo2()
    # print(greet_name.__dict__)
    Person.main()
    pass
