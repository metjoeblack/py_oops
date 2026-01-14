
import math


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x!r}, y={self.y!r})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other: "Vector"):
        return type(self)(
            self.x + other.x,
            self.y + other.y,
        )

    def __mul__(self, scalar: int | float):
        return self.__class__(
            self.x * scalar,
            self.y * scalar,
        )

    def __rmul__(self, scalar: int | float):
        return self * scalar


def use_vector():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1)

    print(v1 + v2)
    print(v1 * 2)
    print(2 * v1)

    print(abs(v2))
    print(bool(v1))


if __name__ == '__main__':
    symbols = '$¢£¥€¤'
    beyond_ascii = [val for val in map(ord, symbols) if val > 127]
    print(beyond_ascii)
    new_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
    print(new_ascii)
    pass
