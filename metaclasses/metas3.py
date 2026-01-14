
"""A normal class instance can serve as a metaclass too"""


class MetaObj:
    def __call__(self, classname, supers, classdict):
        print("In MetaObj.call: ", classname, supers, classdict, sep='\n\t', end="\n" * 2)
        a_class = self.__my_new__(classname, supers, classdict)
        self.__my_init__(a_class, classname, supers, classdict)
        return a_class

    def __my_new__(self, classname, supers, classdict):
        print("In MetaObj.my_new: ", classname, supers, classdict, sep='\n\t', end="\n" * 2)
        return type(classname, supers, classdict)

    def __my_init__(self, a_class, classname, supers, classdict):
        print("In MetaObj.my_init: ", classname, supers, classdict, sep='\n\t', end="\n" * 2)
        print("...init class object: ", list(a_class.__dict__.keys()))


class Super:
    pass


print("Making class")
class Hack(Super, metaclass=MetaObj()):
    data = 1

    def method(self, arg):
        return self.data + arg


print("Making instance")
x = Hack()
print(f"Attrs: {x.data}, {x.method(2)}")







