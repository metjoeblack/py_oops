

class Meta(type):
    def __new__(cls, classname, supers, classdict):
        return type.__new__(cls, classname, supers, classdict)


class MetaOne(type):
    def __new__(cls, classname, supers, classdict):
        print(f"\n{'inside meta.new'.center(80, '-')}")
        print("In MetaOne.new:", cls,  classname, supers, classdict, sep="\n\t")
        print(f"{'inside meta.new'.center(80, '-')}\n")
        return type.__new__(cls, classname, supers, classdict)


class Super:
    pass


print("Making class")
class Hack(Super, metaclass=MetaOne):
    data = 1

    def __init__(self, value):
        print(f"{'Hack init'.center(60, '*')}")
        self.value = value

    def method(self, arg):
        return self.data + arg


print("Making Instance")
x = Hack(12)
print(f"x attribute: {x.data=}, {x.method(2)=}")
print(Hack.__dict__)
print(x.__dict__)
