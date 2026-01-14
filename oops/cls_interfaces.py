
from abc import ABCMeta, abstractmethod


class SuperKlass(metaclass=ABCMeta):
    def method(self):
        print(self)
        print("In SuperKlass.method")

    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        pass


class Provider(SuperKlass):
    def action(self):
        print(self)
        print("In Provider.action")


if __name__ == "__main__":
    x = Provider()
    x.delegate()





