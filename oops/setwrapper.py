
class Set:
    def __init__(self, values=None):
        if values is None:
            values = []
        self.data = []
        self.__concat(values)

    def __concat(self, values):
        for val in values:
            if val not in self:
                self.data.append(val)

    def intersect(self, other):
        return type(self)(val for val in self if val in other)

    def __and__(self, other):
        return self.intersect(other)

    def union(self, other):
        res = self.data[:]
        for val in other:
            if val not in res:
                res.append(val)
        return type(self)(res)

    def __or__(self, other):
        return self.union(other)

    def __contains__(self, value):
        return True if value in self.data else False

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"({', '.join(str(val) for val in self)})"
        )

    @staticmethod
    def main():
        x = Set([1, 2, 3, 5, 7])
        y = Set([1, 3, 6, 7, 8])
        z = Set()
        print(z)
        print(x)
        print(x.union(y))
        print(x | y)
        print(x & y)
        print(x.intersect(y))
        print(x[2])


class SetWrapper(list):
    def __init__(self, values=None):
        list.__init__(self)
        if values is None:
            values = []
        try:
            iter(values)
        except TypeError:
            raise TypeError("SetWrapper can only handle iterables")
        self.__concat(values)

    def __concat(self, values):
        for val in values:
            if val not in self:
                self.append(val)

    def intersect(self, other):
        return type(self)(val for val in self if val in other)

    def __and__(self, other):
        return self.intersect(other)

    def union(self, other):
        res = (myself := type(self))(self)      # copy me and my list
        res.__concat(other)
        return myself(res)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"({', '.join(repr(val) for val in self)})"
        )

    @staticmethod
    def main():
        x = SetWrapper([1, 2, 3, 4])
        y = SetWrapper([3, 4, 5])
        t = SetWrapper()
        print(x)
        print(t)
        print(x & y)
        print(x.intersect(y))
        print(x | y)
        print(x.union(y))
        # print(x[2])
        z = SetWrapper("hello")
        print(z[0], z[-1], z[2:])

        for c in z:
            print(c, end=", ")
        print(''.join(c.upper() for c in z))
        print(len(z))
        print(z)

        print(z & "mello")
        print(z | "mello")


if __name__ == "__main__":
    # Set.main()
    SetWrapper.main()
    pass
