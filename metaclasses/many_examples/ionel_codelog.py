
"""
https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses
"""
from pprint import pprint


def display_locals(method_name, local_scope):
    print(f"{f'Inside {method_name}'.center(80, '-')}")
    for key, value in local_scope.items():
        if key == "classdict":
            pprint(value, indent=4)
        else:
            print(f"{key} = {value!r}")
    print(f"{f'Inside {method_name}'.center(80, '-')}\n")


class Meta(type):

    @classmethod
    def __prepare__(metacls, classname, supers, **kwargs):
        display_locals("Meta.__prepare__", locals())
        return {}

    def __new__(metacls, classname, supers, classdict, **kwargs):
        display_locals("Meta.__new__", locals())
        return type.__new__(metacls, classname, supers, classdict)

    def __init__(cls, classname, supers, classdict, **kwargs):
        display_locals("Meta.__init__", locals())
        super().__init__(classname, supers, classdict)

    def __call__(cls, *args, **kwargs):
        display_locals("Meta.__call__", locals())
        return type.__call__(cls, *args, **kwargs)


class MyClass(metaclass=Meta, extra=1):
    my_class_attr = "For fun"

    def __new__(cls, *args, **kwargs):
        display_locals("MyClass.__new__", locals())
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        self.instance_attr = args[0]
        display_locals("MyClass.__init__", locals())
        super().__init__()

    def __str__(self):
        return f"<Instance of MyClass: {getattr(self, 'instance_attr', 'MISSING!')}>"

    def just_method(self):
        return f"{self.__class__.__name__}({self.instance_attr})"


if __name__ == '__main__':
    my_class = MyClass(100000000, akwarg="Keyword_Argument")
    pass
