
class Tracer:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Calling {self.func.__name__!r} => {self.num_calls} times")
        return self.func(*args, **kwargs)


def tracer(func):
    def on_call(*args, **kwargs):
        on_call.num_calls += 1
        print(f"Calling {on_call.num_calls} to {func.__name__!r}")
        return func(*args, **kwargs)
    on_call.num_calls = 0
    return on_call


@Tracer
def hack(a, b, c=1):
    return a + b + c


class C:
    @tracer
    def hack(self, a, b, c=1):
        return a + b + c

    @staticmethod
    def main():
        x = C()
        print(x.hack(1, 2, 3))
        print(x.hack("a", "b", "c"))


def decorator(cls):
    class Proxy:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)
        def __getattr__(self, attr_name):
            return getattr(self.wrapped, attr_name)
    return Proxy


@decorator
class M:
    pass


if __name__ == '__main__':
    # print(hack(1, 2))
    # print(hack("a", "b", "c"))
    pass
