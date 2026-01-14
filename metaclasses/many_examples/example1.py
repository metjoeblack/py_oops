

class Foo:
    """Foo = type("Foo", (), {})"""
    pass


class Bar(Foo):
    """Bar = type("Bar", (Foo,), dict(attr=100))"""
    attr = 100

    @staticmethod
    def main():
        b = Bar()
        print(Bar.attr, b.attr)
        print(b.__class__)
        print(b.__class__.__bases__)


class NewFoo:
    """
    NewFoo = type(
        "NewFoo",
        (),
        {
            "attr": 100,
            "attr_val": (lambda obj: obj.attr),
        }
    )
    """
    attr = 100

    def attr_val(self):
        return self.attr

    @staticmethod
    def main():
        x = NewFoo()
        print(x.attr)
        print(x.attr_val())


def convoluted_func(obj):
    print(f"attr = {obj.attr}")


class AnotherFoo:
    """
    AnotherFoo = type(
        "AnotherFoo",
        (),
        {
            "attr": 100,
            "attr_val": convoluted_func,
        }
    )
    """
    attr = 100
    attr_val = convoluted_func

    @staticmethod
    def main():
        x = AnotherFoo()
        print(x.attr)
        print(AnotherFoo.attr_val(x))


if __name__ == '__main__':
    # Bar.main()
    AnotherFoo.main()
    pass






