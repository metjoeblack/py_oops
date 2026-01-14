

class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, attr_name):
        print(f"Trace: {attr_name}")
        return getattr(self.wrapped, attr_name)


if __name__ == "__main__":
    x = Wrapper([1, 2, 3, 4])
    x.append(5)
    print(x.wrapped)