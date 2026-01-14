
import operator


class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        # print(cls, args, kwargs)
        super().__init__(*args, **kwargs)
        for idx, arg_name in enumerate(getattr(cls, "_fields")):
            setattr(cls, arg_name, property(operator.itemgetter(idx)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []
    def __new__(cls, *args):
        if len(cls._fields) != len(args):
            raise TypeError(f"{len(cls._fields)} fields required.")
        return tuple.__new__(cls, args)


class Stock(StructTuple):
    _fields = ["name", "shares", "price"]


class Point(StructTuple):
    _fields = ["x", "y",]


if __name__ == '__main__':
    s = Stock("ACME", 50, 91.1)
#     # print(s.name, s.shares, s.price)
#     print(s)