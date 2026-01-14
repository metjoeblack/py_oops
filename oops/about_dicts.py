
from pprint import pprint
import logging


class DemoClass:
    class_attr = "This is a class attribute"

    def __init__(self):
        self.instance_attr = "This is an instance attribute"

    def method(self):
        return f"{self.__class__.__name__}.This is a method"


def introspect_demo():
    pprint(DemoClass.__dict__)  # vars(DemoClass)
    pprint(DemoClass.__dict__.get("__dict__"))
    pprint(DemoClass.__dict__.get("__static_attributes__"))
    dc = DemoClass()
    print(dc.__dict__)

    pprint(int.__dict__)
    pprint(dict.__dict__)


class Config:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    update = __init__

    def __str__(self):
        return str(vars(self))


def introspect_config():
    config = Config(theme='light', font='Arial', language='English')
    print(config)

    user_conf = {"theme": "dark", "font_size": 14, "language": "Spanish"}
    config.update(**user_conf)

    print(config)


class Parent:
    def __init__(self):
        self.parent_attr = "This is parent instance attribute"


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attr = "This is child instance attribute"

    @staticmethod
    def main():
        child = Child()
        print(child.__dict__)


def fibonacci(n):
    """Fibonacci Sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ..."""
    cache = vars(fibonacci).setdefault("cache", dict())
    if n not in cache:
        cache[n] = 1 if n <= 2 else fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


class Record:
    def __init__(self, **fields):
        logging.info(f"[INIT] Creating record with fields: {fields}")
        vars(self).update(fields)

    def __getattribute__(self, attr_name):
        if attr_name == '__dict__':
            return super().__getattribute__(attr_name)
        value = object.__getattribute__(self, attr_name)
        logging.info(f"[GETATTRIBUTE] Accessing {attr_name!r} => {value!r}")
        return value

    def __setattr__(self, attr_name, value):
        if attr_name in vars(self):
            logging.info(f"[UPDATE] Modifying {attr_name!r} => {value!r}")
        else:
            logging.info(f"[SET] Creating {attr_name!r} => {value!r}")
        object.__setattr__(self, attr_name, value)

    def __delattr__(self, attr_name):
        if attr_name in vars(self):
            logging.info(f"[DEL] Deleting {attr_name!r}")
            del vars(self)[attr_name]
        else:
            logging.warning(
                f"[DEL] Attempted to delete non-existent field: {attr_name!r}"
            )

    @staticmethod
    def main():
        jane = Record(first_name="Jane", last_name="Doe", age=25)
        print(vars(jane))
        print(jane.first_name)
        print(jane.age)

        jane.age = 26
        jane.job = "Software Engineer"

        del jane.last_name

        print(jane.__dict__)


class Vector:
    def __init__(self, **coords):
        private_coords = {f"_{key}": value for key, value in coords.items()}
        vars(self).update(private_coords)

    def __getattr__(self, attr_name):
        private_attr = f"_{attr_name}"
        try:
            return vars(self)[private_attr]
        except KeyError:
            raise AttributeError(
                f"{type(self).__name__!r} has no attribute {attr_name!r}"
            ) from None

    def __repr__(self):
        fields = (
            f"{k.lstrip('_')}={v}" for k, v in sorted(vars(self).items())
        )
        return f"{type(self).__name__}({', '.join(fields)})"


class ColoredVector:
    COLORED_INDEXES = ("red", "green", "blue")

    def __init__(self, red, green, blue, **coords):
        super().__init__(**coords)
        vars(self)['color'] = [red, green, blue]

    def __getattr__(self, attr_name):
        try:
            channel = ColoredVector.COLORED_INDEXES.index(attr_name)
        except ValueError:
            return super().__getattr__(attr_name)
        else:
            return vars(self)['color'][channel]

    def __setattr__(self, attr_name, value):
        try:
            channel = ColoredVector.COLORED_INDEXES.index(attr_name)
        except ValueError:
            super().__setattr__(attr_name, value)
        else:
            vars(self)['color'][channel] = value


def main():
    v = Vector(p=9, q=10)
    print(v)
    print(v.__dict__)
    print(v.p, v.q)
    # print(v.x)


if __name__ == '__main__':
    # introspect_config()
    # Child.main()
    # print(fibonacci(10))
    # Record().main()
    pass
