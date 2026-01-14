
class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(name={self.name!r}, salary={self.salary:,.2f})"
        )

    def give_rise(self, percent):
        self.salary += self.salary * percent

    def work(self):
        print(f"{self.name!r} does stuff.")


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, salary=50_000)

    def work(self):
        print(f"{self.name!r} makes food.")


class Server(Employee):
    def __init__(self, name):
        # Employee.__init__(self, name, salary=40_000)
        super().__init__(name, salary=40_000)

    def work(self):
        print(f"{self.name!r} interfaces with customer.")


class PizzaRobot(Chef):
    def __init__(self, name):
        # Chef.__init__(self, name)
        super().__init__(name)

    def work(self):
        print(f"{self.name!r} makes pizza.")


if __name__ == "__main__":
    pat = PizzaRobot("Pat")
    print(pat)
    pat.work()
    pat.give_rise(.20)
    print(pat); print()

    for klass in (Employee, Chef, Server, PizzaRobot):
        instance = klass(klass.__name__)
        instance.work()
