
from collections import OrderedDict


class NoDuplicateOrderedDict(OrderedDict):
    def __init__(self, classname):
        self.classname = classname
        super().__init__()

    def __setitem__(self, key, value):
        if key in self:
            raise TypeError(f"{key!r} already defined in {self.classname!r}")
        super().__setitem__(key, value)


class OrderedMeta(type):
    @classmethod
    def __prepare__(cls, classname, supers):
        return NoDuplicateOrderedDict(classname)

    def __new__(cls, classname, supers, classdict):
        attr_order = tuple(
            attr_name for attr_name in classdict
            if not attr_name.startswith("_")
        )
        classdict |= {"_attr_order": attr_order}
        return type.__new__(cls, classname, supers, classdict)


class A(metaclass=OrderedMeta):
    def spam(self):
        pass

    def foo(self):
        pass


if __name__ == '__main__':
    a = A()
    a.spam()





