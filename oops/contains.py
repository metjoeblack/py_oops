
def trace(msg, end=""):
    print(msg, end=end)


class Iters:
    def __init__(self, value):
        self.data = value

    def __iter__(self):
        trace(f"@iter")
        self.idx = 0
        return self

    def __getitem__(self, idx):
        trace(f"@get[{idx}]")
        return self.data[idx]

    def __next__(self):
        trace(f"@next")
        if self.idx == len(self.data):
            raise StopIteration

        item = self.data[self.idx]
        self.idx += 1
        return item

    def __contains__(self, item):
        trace(f"@contains[{item}]")
        return item in self.data


def self_test(it):
    x = it([1, 2, 3, 4])
    tests = "In", "For", "Comp", "Map", "Manual"
    for test in tests:
        trace(test.ljust(max(map(len, tests)) + 3))
        match test:
            case "In":                          # __contains__
                trace(3 in x)
            case "For":                         # __iter__, __next__
                for i in x:
                    trace(i, end="| ")
            case "Comp":
                trace([i ** 2 for i in x])
            case "Map":
                trace(list(map(bin, x)))
            case "Manual":
                i = iter(x)
                while True:
                    try:
                        trace(next(i), end="| ")
                    except StopIteration:
                        break
        print()


if  __name__ == "__main__":
    self_test(Iters)