"""Assorted class utilities and tools"""


class AttrsDisplay:
    """
    Provides an inheritable display overload method that shows
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its class). Can be mixed into any class, and
    will work on any instance.
    """
    def __gather_attrs(self):
        return ', '.join(
            f"{key}={getattr(self, key)!r}"
            for key in sorted(vars(self).keys())
        )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__gather_attrs()})"


if __name__ == '__main__':
    class TopTest(AttrsDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    x, y = TopTest(), SubTest()
    print(x)
    print(y)