
from typing import Any


class Widget:
    """
    class Widget(object, metaclass=type):
        pass

    classname = "Widget"
    metaclass = type
    super_classes = ()
    kwargs = {}
    namespace = metaclass.__prepare__(classname, super_classes, **kwargs)
    ActualWidget = metaclass.__new__(
        metaclass, classname, super_classes, namespace, **kwargs
    )
    metaclass.__init__(
        ActualWidget, classname, super_classes, namespace, **kwargs
    )
    """
    pass


def display(content: dict[str, Any]):
    for key, value in content.items():
        if key == "classdict":
            print("\tclassdict: ")
            for k, v in content.get("classdict").items():
                print(f"\t\t{k} = {v!r}")
        else:
            print(f"\t{key} = {value!r}")


class TracingMeta(type):
    @classmethod
    def __prepare__(metacls, classname, super_classes, **kwargs):
        print(f"\n----TracingMeta __prepare__(classname, super_classes, **kwargs)")
        namespace = super().__prepare__(classname, super_classes)
        display(locals())
        return namespace

    def __new__(metacls, classname, super_classes, classdict, **kwargs):
        print(f"\n----TracingMeta.__new__(classname, classdict, super_classes, **kwargs)")
        display(locals())
        return type.__new__(metacls, classname, super_classes, classdict)

    def __init__(cls, classname, super_classes, classdict, **kwargs):
        print(f"\n----TracingMeta.__init__(classname, super_classes, classdict, **kwargs)")
        display(locals())
        super().__init__(classname, super_classes, classdict, **kwargs)

    def __call__(cls, *args, **kwargs):
        print(f"\n----TracingMeta.__call__(*args, **kwargs)")
        display(locals())
        return type.__call__(cls, *args, **kwargs)

    def meta_method(cls):
        print(f"\n----TracingMeta.meta_method(cls) - {cls = }")
        display(locals())
        print()


class TracingClass(metaclass=TracingMeta, extra=100):
    cls_attr = 42

    def __new__(cls, *args, **kwargs):
        print(f"\n----TracingClass.__new__(cls, *args, **kwargs)")
        obj = super().__new__(cls)
        display(locals())
        return obj

    def __init__(self, *args, **kwargs):
        print(f"\n----TracingClass.__init__(*args, **kwargs)")
        display(locals())

    def action(self, message):
        print(f"{self.__class__}, {message}")


class KeywordOnlyMeta(type):

    def __call__(cls, *args, **kwargs):
        if args:
            raise TypeError(
                f'constructor for class {cls.__name__!r} does '
                f'not accept positional arguments'
            )
        return super().__call__(**kwargs)


class ConstrainedToKeywords(metaclass=KeywordOnlyMeta):

    def __init__(self, *args, **kwargs):
        print(f"{args = }")
        print(f"{kwargs = }")
        for key, value in kwargs.items():
            setattr(self, key, value)


if __name__ == '__main__':
    # WidgetView.meta_method()
    t = TracingClass(21, keyword="clef")
    # c = ConstrainedToKeywords(23, 42, 96, color="white")
    # c2 = ConstrainedToKeywords(num = 42, color="white")
    pass

