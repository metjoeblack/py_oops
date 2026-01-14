

class Typed:
    """A set of descriptor for various types."""
    _expected_type = type(None)

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            err_msg = f"{self._name!r} expected {str(self._expected_type)}"
            raise TypeError(err_msg)
        instance.__dict__[self._name] = value


class Integer(Typed):
    _expected_type = int


class Float(Typed):
    _expected_type = float


class String(Typed):
    _expected_type = str


class OrderedMeta(type):
    def __new__(cls, classname, supers, classdict):
        attr_order = [
            attr for attr, attr_value in classdict.items()
            if not attr.startswith("__") and isinstance(attr_value, Typed)
        ]
        classdict |= {"__attr_order": attr_order}
        return type.__new__(cls, classname, supers, classdict)

    @classmethod
    def __prepare__(metacls, classname, supers):
        return dict()


class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ','.join(
            str(getattr(self, name))
            for name in getattr(self, '__attr_order')
        )


class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"({self.name!r}, {self.shares!r}, {self.price!r})"
        )

    @staticmethod
    def main():
        google = Stock("Google", 1000, 590.12)
        print(google.name, google.shares, google.price)
        print(google.as_csv())
        print(google)
        # google.shares = 1001.1

        aapl = Stock("AAPL", 2000, 900.1)
        print(aapl)


if __name__ == '__main__':
    Stock.main()

