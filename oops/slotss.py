
class Limiter:
    __slots__ = ('age', 'name', 'job', '__dict__')
    c = 9

    def __init__(self):
        self.e = 4

    @staticmethod
    def tester():
        i = Limiter()
        # print(i.age)
        i.age = 20
        print(i.age)
        # i.ape = 1000
        i.name = "Jones"
        # print(i.__dict__)     # __slots__ means no __dict__ by default.
        print(getattr(i, "age"))
        setattr(i, "job", "mgr")
        print(getattr(i, "job"))
        print("job" in dir(i))
        print(i.__dict__)
        print(i.__slots__)

        print(getattr(i, "e"))
        print(getattr(i, "c"))

        for attr in [
            *getattr(i, "__slots__", []),
            *getattr(i, "__dict__", [])
        ]:
            print(f"{attr} ==> {getattr(i, attr)}")


class E:
    __slots__ = ('c', 'd')


class D(E):
    __slots__ = ('a', 'c', 'e', '__dict__')

    @staticmethod
    def tester():
        i = D()
        print([attr for attr in dir(i) if not attr.startswith('__')])
        i.a = 1; i.b = 2; i.c = 3
        print(i.a, i.b, i.c)
        print(E.__slots__)
        print(D.__slots__)
        print(i.__slots__)
        print(i.__dict__)


class SlotFul:
    __slots__ = ('a', 'b', '__dict__')

    def __init__(self, data):
        self.c = data

    @staticmethod
    def tester():
        i = SlotFul(3)
        i.a = 1; i.b = 2
        print(i.a, i.b, i.c)

        for attr in (attr for attr in dir(i) if not attr.startswith('__')):
            print(f"{attr} ==> {getattr(i, attr)}")


if __name__ == '__main__':
    # Limiter.tester()
    # D.tester()
    SlotFul.tester()
    pass
