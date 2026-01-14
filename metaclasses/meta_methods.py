
class Meta(type):
    def z(cls):
        print(f"M.z, {cls.__name__}")

    def y(cls):
        print(f"M.y, {cls.__name__}")


class D(metaclass=Meta):
    def y(self):
        print(f"D.y, {self.__name__}")

    def x(self):
        print(f"D.x, {self.__name__}")


if __name__ == '__main__':
    print(D.x)
    print(D.y)
    print(D.z)
    print(D.z())






