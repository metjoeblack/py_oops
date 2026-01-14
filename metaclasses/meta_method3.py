
class Employee:
    rate = 50

    def __init__(self, name, hours):
        self.name = name
        self.hours = hours

    def pay(self):
        return f"{self.name} ==> {self.rate * self.hours}"

    def __iadd__(self, hours):
        self.hours += hours
        return self


class MetaEmployee(type):
    rate = 50

    def pay(cls):
        return f"{cls.name} ==> {cls.rate * cls.hours}"

    def __iadd__(cls, hours):
        cls.hours += hours
        return cls


class Pat(metaclass=MetaEmployee):
    name = "Pat Smith"
    hours = 2_000


Pat2 = MetaEmployee(
    "Pat2",
    (),
    dict(name="Pat2", hours=2_000),
)



if __name__ == '__main__':
    print(Pat.pay())
    Pat += 1_000
    print(Pat.pay())
