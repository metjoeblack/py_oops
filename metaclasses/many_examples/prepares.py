
from functools import wraps
from time import sleep
from typing import Self, Generator

import pytest


class WrapStackPreparer(dict):
    """
    First define the DictLike class.

    1. In the __init__, we expect a parameter array_wraps that contains each
        the wrappers to apply.

    2. In the __setitem__, we alter the default behavior of the dict class.
        2.1 This method will be executed every time a class attribute is
            registered or a method in the class is being 'prepared'.
        2.2 If it is a class attribute, nothing will happen. On the other hand
            for methods, which are callable, we will wrap them.
        2.3 Finally we invoke the dict.__setitem__ method that will register
            the already encapsulated method.

    """
    def __init__(self, array_wraps):
        super().__init__()
        self.array_wraps = array_wraps

    def __setitem__(self, key, value):
        if callable(value):
            for wrap in self.array_wraps:
                value = wrap(value)
        dict.__setitem__(self, key, value)


class MetaWrap(type):
    """
    1. We define __prepare__ as classmethod returning the DictLike and
       propagating **kwargs so that, as we will see later, we send the
       array of wraps.
    2. We define a standard __new__, without customizing anything, to
       build the class.
    """
    @classmethod
    def __prepare__(metacls, classname, supers, **kwargs):
        return WrapStackPreparer(**kwargs)

    def __new__(metacls, classname, supers, classdict, **kwargs):
        a_class = type.__new__(metacls, classname, supers, classdict)
        return a_class


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Start calling function - {func.__name__!r}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__!r}")
        return result
    return wrapper


class LoggedClass(metaclass=MetaWrap, array_wraps=[logged]):

    def method1(self):
        sleep(0.1)
        print(f"{self.__class__.__name__}, Method 1 called")

    def method2(self):
        sleep(0.5)
        print(f"{self.__class__.__name__}, Method 2 called")

    def main(self):
        self.method1()
        self.method2()


if __name__ == '__main__':
    logged_cl = LoggedClass()
    print("Calling directly")
    logged_cl.method1()
    logged_cl.method2()
    print("Calling from main:")
    logged_cl.main()