
class Rec:
    pass


def inspect_class():
    Rec.name = "Pat"
    Rec.age = 20
    print(Rec.age, Rec.name)

    x = Rec()
    y = Rec()
    x.name = "X"
    print(x.name, x.age)
    x.name = "Sue"
    print(Rec.name, x.name, y.name)
    print(Rec.__dict__)
    print(x.__dict__)
    print(x.__dict__["name"])
    print(x.age)
    print(x.__dict__["age"])


class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age

    def info(self):
        return self.name, self.jobs


if __name__ == '__main__':
    inspect_class()
    pass









