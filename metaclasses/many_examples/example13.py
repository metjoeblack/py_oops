
import weakref



class NoInstancesMeta(type):
    def __call__(cls, *args, **kwargs):
        raise TypeError("Can't instantiate directly.")


class Spam(metaclass=NoInstancesMeta):
    @staticmethod
    def grok(x):
        print(f"Spam.grok({x})")


class SingletonMeta(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class Foo(metaclass=SingletonMeta):
    def __init__(self):
        print(f"{self.__class__.__name__}")

    @staticmethod
    def main():
        a = Foo()
        b = Foo()
        print(a is b)


class CachedMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.__cache = weakref.WeakValueDictionary()

    def __call__(cls, *args):
        if args in cls.__cache:
            return cls.__cache[args]
        else:
            a_class = super().__call__(*args)
            cls.__cache[args] = a_class
            return a_class


class NewSpam(metaclass=CachedMeta):
    def __init__(self, name):
        self.name = name
        print(f"Creating Spam{name!r}")


if __name__ == '__main__':
    # Spam.grok(42)
    # spam = Spam()
    a = NewSpam("Guido")
    b = NewSpam("Diana")
    c = NewSpam("Guido")    # Same object, cached.
    print(a is b, a is c)
    pass





