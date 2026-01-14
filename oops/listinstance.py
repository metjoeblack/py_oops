

class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of instance via
    inheritance of __str__ coded here. Displays instance attributes only;
    self is instance of lowest class; __X naming avoids clashing with
    client's attributes. Works for classes with slots: a __dict__ is ensured
    by lack of slots here.
    """
    def __get_attribute_names(self):
        return "".join(
            f"\t{attr}={self.__dict__.get(attr)!r}\n"
            for attr in sorted(self.__dict__)
        )

    def __get_one_level_superclass(self):
        return ", ".join(sup.__name__ for sup in self.__class__.__bases__)

    def __str__(self):
        return (
            f"<Instance of {self.__class__.__name__}"
            f"({self.__get_one_level_superclass()}), "
            f"address {id(self):#x}:\n"
            f"{self.__get_attribute_names()}>"
        )


if __name__ == "__main__":
    class Person(ListInstance):
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Student(Person):
        def __init__(self, name, age, grade):
            super().__init__(name, age)
            self.grade = grade

    s = Student("John", 12, 6)
    print(s)
