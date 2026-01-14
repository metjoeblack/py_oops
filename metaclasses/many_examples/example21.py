

class TypeDescriptor:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name.strip('_')!r} must be a {self.expected_type}"
            )
        vars(instance)[self.name] = value


class Person:
    name = TypeDescriptor(str)
    age = TypeDescriptor(int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    p = Person("John Nash", 18)
    print(p.name)
    print(p.age)
    # print(vars(p))

