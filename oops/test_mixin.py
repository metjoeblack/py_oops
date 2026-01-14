"""
Generic lister-mixin tester: similar to transitive reloader in
Chapter 25, but passes a class object to tester (not function),
and test_by_names adds loading of both module and class by name
strings here, in keeping with Chapter 31's factories pattern.
"""

import importlib


def tester(lister_class, sept=False):
    """Pass any lister class to lister_class"""

    class Super:
        def __init__(self):
            self.data1 = "code"

        def method1(self):
            pass

    class Sub(Super, lister_class):
        def __init__(self):
            Super.__init__(self)
            self.data2 = "Python"
            self.data3 = "3.12"

        def method2(self):
            pass


    instance = Sub()
    print(instance)
    if sept:
        print(f"\n{'-' * 80}\n")


def test_by_names(mod_name, class_name, sept=False):
    module_obj = importlib.import_module(mod_name)
    lister_class = getattr(module_obj, class_name)
    tester(lister_class, sept=sept)


if __name__ == "__main__":
    test_by_names("listinstance", "ListInstance", True)
    test_by_names("listinherited", "ListInherited", True)
    test_by_names("listtree", "ListTree", False)