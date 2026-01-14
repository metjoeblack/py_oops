
from example16 import make_signatures
import inspect


class StructureMeta(type):
    def __new__(metacls, classname, supers, classdict, **kwargs):
        classdict['__signature__'] = make_signatures(*classdict.get('_fields', []))
        return type.__new__(metacls, classname, supers, classdict)


class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound_values = getattr(self, "__signature__").bind(*args, **kwargs)
        for arg_name, arg_value in bound_values.arguments.items():
            setattr(self, arg_name, arg_value)

    def __repr__(self):
        fields = ", ".join(
            f"{attr}={attr_val!r}" for attr, attr_val in vars(self).items()
        )
        return (
            f"{self.__class__.__name__}"
            f"({fields})"
        )


class Stock(Structure):
    _fields = ["name", "shares", "price"]


class Point(Structure):
    _fields = ["x", "y"]


if __name__ == '__main__':
    s1 = Stock("Google", 100, 490.1)
    print(s1)
    print(inspect.signature(Stock))
    print(inspect.signature(Point))