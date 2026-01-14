
from inspect import signature
import logging


class MatchSignatureMeta(type):
    def __init__(cls, classname, supers, classdict):
        type.__init__(cls, classname, supers, classdict)
        sup = super(cls, cls)
        for name, value in classdict.items():
            if name.startswith('_') or not callable(value):
                continue

            prev_definition = getattr(sup, name, None)
            if prev_definition is not None:
                prev_sig = signature(prev_definition)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning(
                        f"Signature mismatch for in "
                        f"{value.__qualname__}.{prev_sig} != {val_sig}"
                    )


class RootClass(metaclass=MatchSignatureMeta):
    pass


class A(RootClass):
    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass


class B(A):
    def foo(self, a, b):
        pass

    def spam(self, x, z):
        pass
