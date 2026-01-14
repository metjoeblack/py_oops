
from pprint import pprint


class Fibonacci:
    def __init__(self):
        self.cache = dict.fromkeys(range(2), 1)

    def __call__(self, number):
        if number not in self.cache:
            self.cache[number] = self(number - 1) + self(number - 2)
        return self.cache.get(number)


def cube(base):
    result = base ** 3

    def inner_func():
        a = 2
        print(result * a)
    print(dir())
    print(vars())
    print(locals())
    print(f"The result is {result}")


if __name__ == '__main__':
    # fibo = Fibonacci()
    # print(fibo(5))
    # cube(3)
    pprint(__builtins__.__dict__)
    pass
