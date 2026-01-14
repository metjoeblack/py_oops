
def appreciate_type():
    print(type([]))
    print(type(type([])))
    print([].__class__, [].__class__.__class__, sep='\t')


class SuperClass:
    super_cls_attr = 0.0


class Hack(SuperClass):
    cls_attr = 1

    def method(self, arg):
        return self.cls_attr + arg


def how_type_create_class():
    D = type(
        'Hack',
        (),
        {
            "data": 1,
            "method": (lambda self, arg: self.data + arg)
        },
    )

    d = D()
    print(d.data)
    print(d.method(2))
    print(d)
    print(D)
    print(D.__bases__)
    print(d.__class__.__mro__)
    print([attr for attr in dir(d) if not attr.startswith('__')])
    print(
        [
            (attr_name, value)
            for attr_name, value in D.__dict__.items()
            if not attr_name.startswith('__')
        ]
    )


class Super:
    pass


class CustomMeta(type):
    def __new__(cls, classname, supers, attributedict):
        return type.__new__(cls, classname, supers, attributedict)


class MyHack(Super, metaclass=CustomMeta):
    """Notice the MyHackNew below."""
    data = 1

    def method(self, arg):
        return self.data + arg


MyHackNew = CustomMeta(
    "MyHackNew",
    (Super, ),
    {
        "data": 1,
        "method": lambda self, arg: self.data + arg,
        "__module__": "__main__",
    }
)

my = MyHackNew()
print(my.data, my.method(2))
print(MyHackNew.__dict__)
