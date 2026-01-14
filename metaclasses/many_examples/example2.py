

def new(cls):
    a_class = object.__new__(cls)
    a_class.attr = 100
    return a_class


class Foo:
    __new__ = new

    @staticmethod
    def main():
        f = Foo()
        print(f.attr)

        g = Foo()
        print(g.attr)


class Meta(type):
    def __new__(cls, classname, supers, classdict):
        a_class = type.__new__(cls, classname, supers, classdict)
        a_class.attr = 100
        return a_class


class AnotherFoo(metaclass=Meta):
    pass

    @staticmethod
    def main():
        f = AnotherFoo()
        print(f.attr)


class AnotherMeta(type):
    def __init__(cls, classname, supers, classdict):
        type.__init__(cls, classname, supers, classdict)
        cls.attr = 100


class X(metaclass=AnotherMeta):
    pass


class Y(metaclass=AnotherMeta):
    pass


class Z(metaclass=AnotherMeta):
    pass


if __name__ == '__main__':
    # Foo.main()
    # AnotherFoo.main()
    print(X.attr, Y.attr, Z.attr)
    pass



