
class Printer:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value!r})"


class Commutative:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value!r})"

    def __add__(self, other):
        if isinstance(other, type(self)):
            other = other.value
        return type(self)(self.value + other)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        # raise NotImplemented("Not implemented")
        self.value += other
        return self


if __name__ == "__main__":
    # objs = [Printer(2), Printer(3)]
    # for obj in objs:
    #     print(obj)
    #     print(repr(obj))
    pass
    c = Commutative(5)
    d = Commutative(6)
    print(c + d)
    print(d + c)
    print(c + 2)
    print(3 + d)
    c += 10
    print(c)