
import types
import operator
import sys


def named_tuple(classname, fieldnames):
    classdict = {
        name: property(operator.itemgetter(idx))
        for idx, name in enumerate(fieldnames)
    }

    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError(f"Expected {len(fieldnames)} arguments, got {len(args)}")
        return tuple.__new__(cls, args)

    classdict['__new__'] = __new__

    a_class = types.new_class(
        classname,
        (tuple,),
        {},
        exec_body=lambda ns: ns.update(classdict)
    )
    a_class.__module__ = sys._getframe(1).f_globals['__name__']
    return a_class


if __name__ == '__main__':
    Point = named_tuple('Point', ('x', 'y'))
    print(Point)
    p = Point(4, 5)
    print(p)
    print(len(p))






