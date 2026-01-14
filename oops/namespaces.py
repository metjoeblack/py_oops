

class SuperKlass:
    def hello(self):
        self.data1 = "hack"


class SubKlass(SuperKlass):
    def hola(self):
        self.data2 = "code"


if __name__ == "__main__":
    x = SubKlass()
    y = SubKlass()
    print(x.__dict__)
    x.hola()
    print(x.__dict__)
    x.hello()
    print(x.__dict__)
    print(x.__class__)
    print(x.data1, x.__dict__["data1"])

    print(SubKlass.__bases__)
    print(SuperKlass.__bases__)

    print(y.__dict__)

    print(list(SuperKlass.__dict__.keys()))
    print(list(SubKlass.__dict__.keys()))
    print(dir(x))



