
from abc import ABCMeta



class SwordMeta(type):
    def __subclasscheck__(self, subclass):
        return (
            hasattr(subclass, "swipe") and callable(subclass.swipe)
            and
            hasattr(subclass, "sharpen") and callable(subclass.sharpen)
        )

    def __instancecheck__(cls, instance):
        return issubclass(type(instance), cls)


class Sword(metaclass=SwordMeta):
    pass


class BroadSword:

    def swipe(self):
        print(f"{self.__class__.__name__} swipe")

    def sharpen(self):
        print(f"{self.__class__.__name__} sharpen")


class SamuraiSword:

    def swipe(self):
        print(f"{self.__class__.__name__} swipe")

    def sharpen(self):
        print(f"{self.__class__.__name__} sharpen")


class Rifle:

    def fire(self):
        print(f"{self.__class__.__name__} fire")


class SwordV2(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, __subclass):
        return (
            hasattr(__subclass, "swipe") and callable(__subclass.swipe)
            and
            hasattr(__subclass, "sharpen") and callable(__subclass.sharpen)
        )


if __name__ == '__main__':
    print(issubclass(BroadSword, SwordV2))
    print(issubclass(SamuraiSword, SwordV2))
    print(issubclass(Rifle, SwordV2))

    samurai = SamuraiSword()
    print(isinstance(samurai, SamuraiSword))
    print(isinstance(samurai, Sword))
    pass