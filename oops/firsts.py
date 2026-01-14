
class FirstClass:

    def __init__(self, value):
        self.data = value

    def display(self):
        print(f"In {self.__class__.__name__}, data = {self.data}")


class SecondClass(FirstClass):
    def display(self):
        print(f"In {self.__class__.__name__}, data = {self.data}")


class ThirdClass(SecondClass):
    def __init__(self, value):
        super().__init__(value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"

    def __add__(self, other):
        return self.__class__(self.data + other.data)

    def mul(self, value):
        self.data *= value


if __name__ == '__main__':
    first = FirstClass("first")
    second = SecondClass("second")
    first.display()
    second.display()

    a = ThirdClass(3)
    a.display()
    b = ThirdClass(4)
    b.display()
    c = a + b
    print(c)
    c.display()

    a.mul(5)
    print(a)



