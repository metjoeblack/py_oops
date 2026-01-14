

class MetaTwo(type):
    def __new__(metacls, classname, supers, classdict):
        print()
        print("\nIn MetaTwo.new:", metacls, classname, supers, classdict, sep="\n\t")
        return type.__new__(metacls, classname, supers, classdict)

    def __init__(cls, classname, supers, classdict) -> None:
        super().__init__(cls)
        print()
        print("\nIn MetaTwo.init: ", cls, classname, supers, classdict, sep="\n\t")
        print(f'...init class object: {list(cls.__dict__.keys())}')


class Super:
    pass


print("Making class")
class Hack(Super, metaclass=MetaTwo):
    data = 1

    def method(self, arg):
        return self.data + arg


print('\nMaking instance')
x = Hack()
print(f"Attrs: {x.data}, {x.method(3)}")


