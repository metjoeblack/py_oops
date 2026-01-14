
class Indexer:
    def __init__(self, data):
        self.data = list(data)

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            print(
                f"slice: start={idx.start}, "
                f"stop={idx.stop}, step={idx.step}"
            )
        return self.data[idx]

    def __setitem__(self, idx, val):
        self.data[idx] = val

    def __index__(self):
        return 255


class Square:
    """one-single scan iteration"""
    def __init__(self, start, stop):
        self.current_val = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_val == self.stop:
            raise StopIteration
        self.current_val += 1
        return self.current_val ** 2


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        item = self.wrapped[self.offset]
        self.offset += 1
        return item


class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


class SkipObjectsYield:
    """multiscan version"""
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        offest = 0
        while offest < len(self.wrapped):
            item = self.wrapped[offest]
            offest += 1
            yield item


class SquareYield:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2


if __name__ == "__main__":
    xy = SquareYield(1, 3)
    for i in xy:
        for j in xy:
            print(f"{i}:{j}", end=" ")
        print()
    pass