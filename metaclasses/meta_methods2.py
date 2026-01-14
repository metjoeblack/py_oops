
class Meta(type):
    def a(cls):
        cls.x = cls.y + cls.z


class D(metaclass=Meta):
    y = 11
    z = 22

    @classmethod
    def b(cls):
        return cls.x


def tester_1():
    D.a()
    print(D.x)

    instance = D()
    print(instance.x, instance.y, instance.z)
    print(instance.b())

    # print(instance.a())


class Meta2(type):
    def __getitem__(cls, idx):
        """This applies to classes"""
        return cls.data[idx]


class E(metaclass=Meta2):
    data = "Hack"

    def __getitem__(self, idx):
        """This applies to nonclass instances"""
        return self.data[idx]


def tester_2():
    print(E[0])
    # print(E.__getitem__)

    i = E()
    print(i.data, E.data)
    print(i.__getitem__, E.__getitem__, sep="\n")
    print(i[0])




if __name__ == '__main__':
    # tester_1()
    tester_2()
    pass




