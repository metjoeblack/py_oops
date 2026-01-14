import collections
import pprint


def trace(label, x, end="\n"):
    print(f"{label}\n{pprint.pformat(x)}{end}")


def filter_dict_vals(dictionary, value):
    """
    Dict 'dictionary' with entries for 'value' removed.
    filter_dict_vals(dict(a=1, b=2, c=1), 1)  ==> {'b': 2}
    """
    return {
        k: v for k, v in dictionary.items() if v != value
    }


def invert_dict(dictionary):
    """
    Dict 'dictionary' with values changed to keys (grouped by values).
    Values must all be hashable to work as dict/set keys.
    invert_dict(dict(a=1, b=2, c=1)) ==> {1:['a', 'c'], 2:['b']}
    """
    new_dict = collections.defaultdict(list)
    for key, value in dictionary.items():
        new_dict[value].append(key)
    return new_dict


def dflr(cls):
    """
    Depth-first left-to-right order of class tree at cls.
    Cycle not possible: Python disallows on __bases__ changes.
    """
    here = [cls]
    for sup in cls.__bases__:
        here += dflr(sup)
    return here


def inheritance(instance):
    if hasattr(instance.__class__, "__mro__"):
        return (instance, ) + instance.__class__.__mro__
    else:
        return [instance] + dflr(instance.__class__)


def map_attrs(instance, with_object=False, by_source=False):
    attr2_obj = {}
    inherits = inheritance(instance)
    for attr in dir(instance):
        for obj in inherits:
            if hasattr(obj, "__dict__") and attr in obj.__dict__:
                attr2_obj[attr] = obj
                break

    if not with_object:
        attr2_obj = filter_dict_vals(attr2_obj, object)
    return attr2_obj if not by_source else invert_dict(attr2_obj)


if __name__ == "__main__":
    class D:                #         object
        attr2 = "D"         #           |
    class C(D):             #           D
        attr2 = "C"         #         /    \
    class B(D):             #        B      C
        attr1 = "B"         #         \    /
    class A(B, C):          #            A
        pass                #

    i = A()
    i.attr0 = "I"

    print(f"Py=> {i.attr0=}, {i.attr1=}, {i.attr2=}")
    trace("INHERITANCE", inheritance(i))
    trace("ATTRIBUTES", map_attrs(i))
    trace("SOURCES", map_attrs(i, by_source=True))



