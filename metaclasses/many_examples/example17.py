

def is_dunder_method(name: str) -> bool:
    return True if name.startswith("__") and name.endswith("__") else False


class NoMixedCaseMeta(type):
    def __new__(metacls, classname, supers, classdict):
        for name in classdict:
            if not is_dunder_method(name) and name.lower() != name:
                raise TypeError(f"Bad attribute name {name!r}")
        return type.__new__(metacls, classname, supers, classdict)


class RootClass(metaclass=NoMixedCaseMeta):
    pass


class A(RootClass):
    Class_attr = "good"

    def foo_bar(self):
        return f"{self.__class__.__name__}, foo_bar()"


class B(RootClass):
    def foo_Bar(self):
        return f"{self.__class__.__name__}, foo_Bar()"
