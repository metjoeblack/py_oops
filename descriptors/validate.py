
import time


class ValidateAttribute:
    def __init__(self, expected_type):
        self.expected_type = expected_type
    
    def __set_name__(self, instance, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return vars(instance).get(self.name)
            
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"attribute {self.name!r} must be {self.expected_type!r} type"
                )
        vars(instance)[self.name] = value


class Person:
    name = ValidateAttribute(str)
    age = ValidateAttribute(int)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return str(vars(self))


class LazyProperty:
    
    def __init__(self, func):
        self.func = func
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        func_name = self.func.__name__
        return vars(instance).setdefault(func_name, self.func(instance))


class ExpensiveComputation:
    
    @LazyProperty
    def compute_value(self):
        time.sleep(2)
        return 42


if __name__ == "__main__":
    p = Person("Alice", 22) 
    print(p)
    obj = ExpensiveComputation()
    print(obj.compute_value)
    print(obj.compute_value)
    
