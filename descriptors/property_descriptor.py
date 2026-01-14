

class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print("get_name")
        return self._name

    def set_name(self, name):
        print('set name...')
        self._name = name

    name = MyProperty(get_name, set_name)

    @staticmethod
    def main():
        x = Person("Sue Jones")
        print(x.name)
        print(x.__dict__)
        print(x.get_name())
        x.name = 'Susan Jones'
        print(x.name)
        print(x.__dict__)


if __name__ == '__main__':
    # Person.main()
    pass

