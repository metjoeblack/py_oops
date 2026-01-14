

class Adder:
    def __init__(self, start=None):
        if start is None:
            start = []
        self.data = start

    def add(self, y):
        raise NotImplemented("Not implemented")

    def __add__(self, other):
        return self.add(other)


class ListAdder(Adder):
    def add(self, y):
        return self.data + y


class DictAdder(Adder):
    def add(self, y):
        return self.data | y


def adder():
    x1 = ListAdder([2])
    print(x1.add([1, 3, 4]))
    print(x1 + [2, 3, 4])

    y2 = DictAdder({1: 2, 3: 4})
    print(y2.add({3: 100, 5: 2}))
    print(y2 + {3: 100, 5: 2})


class Animal:
    def reply(self):
        self.speak()

    def speak(self):
        print("blah")


class Mammal(Animal):
    def speak(self):
        print("huh?")


class Cat(Mammal):
    def speak(self):
        print("meow")


class Dog(Mammal):
    def speak(self):
        print("bark")


class Primate(Mammal):
    def speak(self):
        print("Hello world")


class Hacker(Primate):
    pass


if __name__ == '__main__':
    # spot = Cat()
    # spot.reply()
    # hack = Hacker()
    # hack.reply()
    pass




