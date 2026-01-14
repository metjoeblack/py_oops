
from employees import PizzaRobot, Server


class Customer(object):
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(f"{self.name} orders from {server}")

    def pay(self, server):
        print(f"{self.name} pays items to {server}")


class Oven:
    def bake(self):
        print(f"{self.__class__.__name__} bakes")


class PizzaShop:
    def __init__(self):
        self.server = Server("Jan")             # Embed other objects
        self.chef = PizzaRobot("Pat")
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == "__main__":
    scenario = PizzaShop()
    scenario.order("Sue")
    print("-" * 100)
    scenario.order("Bob")
