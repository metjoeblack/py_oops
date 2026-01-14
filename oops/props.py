

class WithOperators:

    def __getattr__(self, attr_name):
        if attr_name == "age":
            print("get age")
            return 20
        else:
            raise AttributeError(attr_name)

    def __setattr__(self, attr_name, value):
        print(f"set: {attr_name!r}={value!r}")
        if attr_name == "age":
            vars(self)['_age'] = value
            # Also： object.__setattr__(self, attr_name, value)
        else:
            self.__dict__[attr_name] = value

    @staticmethod
    def main():
        x = WithOperators()
        print(x.age)
        x.age = 21
        print(x.age, x._age)
        x.job = "coder"
        print(x.__dict__)


class AgeDescriptor:
    def __get__(self, instance, owner):
        return 20

    def __set__(self, instance, value):
        instance._age = value


class Person:
    age = AgeDescriptor()

    def __init__(self, age):
        self.age = age


class Hack:
    num_instances = 0

    def __init__(self):
        Hack.num_instances += 1

    @classmethod
    def get_num_instances(cls):
        return cls.num_instances

    @staticmethod
    def fetch_num_instances():
        return Hack.num_instances


class NewHack:
    num_instances = 0

    def __init__(self):
        self.count_instances()

    @classmethod
    def count_instances(cls):
        cls.num_instances += 1


class NewSub(NewHack):
    num_instances = 0

    def __init__(self):
        NewHack.__init__(self)


class NewOther(NewHack):
    num_instances = 0


if __name__ == "__main__":
    # WithOperators.main()
    x = NewHack()
    y1, y2 = NewSub(), NewSub()
    z1, z2, z3 = NewOther(), NewOther(), NewOther()
    print(x.num_instances)
    print(y1.num_instances, y2.num_instances)
    print(z1.num_instances, z2.num_instances, z3.num_instances)
    print(NewHack.num_instances, NewSub.num_instances, NewOther.num_instances)
    pass







