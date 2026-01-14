

class Privacy:
    privates = set()
    def __setattr__(self, attr_name, value):
        if attr_name in self.privates:
            raise NameError(
                f"attribute {attr_name!r} for "
                f"{self.__class__.__name__!r} isn't allowed"
            )
        else:
            object.__setattr__(self, attr_name, value)


class Test1(Privacy):
    privates = {"age"}


class Test2(Privacy):
    privates = {"pay", "name"}
    def __init__(self):
        self.__dict__["name"] = "Pat"


if __name__ == "__main__":
    x = Test1()
    x.name = "Sue Jones"
    print(x.name)
    # x.age = 20

    y = Test2()
    y.age = 30
    print(y.age)
    # y.name = "Bob Smith"
    print(y.__dict__)


