

class Meta(type):
    def __new__(cls, classname, supers, classdict):
        print(f"In Meta.new: {classname}")
        return type.__new__(cls, classname, supers, classdict)

    def method3(self):
        return f"{self}, {self.__class__.__name__}, Three 3"


class Super(metaclass=Meta):
    def method2(self):
        return f"{self}, {self.__class__.__name__}, Two 2"


class Sub(Super):
    def method1(self):
        return f"{self}, {self.__class__.__name__}, One 1"


def tester1():
    print("Making instance")
    x = Sub()
    print(x.method1())
    print(x.method2())
    # print(x.method3())
    print(Sub.method2(x))
    print(Sub.method3())
    # print(Sub.method3(x))


class MyMeta(type):
    attr = "meta attr"


class D(metaclass=MyMeta):
    pass


def tester2():
    d = D()
    print(D.attr)
    # print(d.atr)
    print(
        'attr' in D.__dict__,
        'attr' in d.__dict__,
        'attr' in MyMeta.__dict__
    )


class M2(type):
    attr4 = 4


class M1(M2):
    attr3 = 3


class S:
    attr2 = 2


class E(S, metaclass=M1):
    attr1 = 1


def tester3():
    x = E()
    print(x.attr1, x.attr2)
    print(E.attr1, E.attr2, E.attr3, E.attr4)
    print(M1.attr3, M1.attr4)
    # print(x.attr3)
    print(E.__class__)
    print(E.__base__)
    print(M1.__base__)
    print(M1.__class__)
    print(x.__class__.attr4)

    print([c.__name__ for c in E.__mro__])
    print([t.__name__ for t in M1.__mro__])


if __name__ == '__main__':
    # tester2()
    tester3()
    pass
