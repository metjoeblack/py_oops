from __future__ import annotations
from itertools import zip_longest, chain
from array import array
import reprlib
import math
from collections.abc import Iterable, Sized
import operator
import functools
from typing import Optional, SupportsFloat


class Vector:
    typecode = "d"
    __match_args__ = ("x", "y", "z", "t")

    def __init__(self, components: Optional[Iterable[float]] = None):
        if components is None:
            components = tuple()
        self._components = array(type(self).typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        components = reprlib.repr(self._components)
        return (
            f"{type(self).__name__}("
            f"{components[components.find('['):-1]})"
        )

    def __add__(self, other: Vector) -> Vector:
        try:
            return type(self)(
                a + b for a, b in zip_longest(self, other, fillvalue=0.0)
            )
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, scalar: SupportsFloat):
        try:
            factor = float(scalar)
        except TypeError:
            return NotImplemented
        return type(self)(n * factor for n in self)

    def __rmul__(self, scalar: SupportsFloat):
        return self * scalar

    def __matmul__(self, other):
        if isinstance(other, Sized) and isinstance(other, Iterable):
            try:
                return sum(a * b for a, b in zip(self, other, strict=True))
            except ValueError:
                raise ValueError("@ operator requires equal length.") from None
        else:
            return NotImplemented

    def __rmatmul__(self, other):
        return self @ other

    def __eq__(self, other: Vector):
        if isinstance(other, Vector):
            try:
                return all(a == b for a, b in zip(self, other, strict=True))
            except ValueError:
                return False
        else:
            return NotImplemented

    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.hypot(*self)

    def __neg__(self):
        return type(self)(-x for x in self)

    def __pos__(self):
        return type(self)(self)

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return type(self)(self._components[key])
        idx = operator.index(key)
        return self._components[idx]

    def __getattr__(self, name):
        cls = type(self)
        try:
            position = cls.__match_args__.index(name)
        except ValueError:
            position = -1
        if 0 <= position < len(self._components):
            return self._components[position]
        err_msg = f"{cls.__name__!r} object has no attribute {name!r}"
        raise AttributeError(err_msg)

    def __setattr__(self, name: str, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.__match_args__:
                error = "read-only attribute {attr_name!r}"
            elif name.islower():
                error = "can't set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ""
            if error:
                err_msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(err_msg)
        super().__setattr__(name, value)

    def angle(self, n):
        r = math.hypot(*self[n:])
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and self[-1] < 0:
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, format_spec=""):
        if format_spec.endswith("h"):   # hyperspherical coordinates
            format_spec = format_spec[:-1]
            coordinates = chain([abs(self)], self.angles())
            outer_fmt = "<{}>"
        else:
            coordinates = self
            outer_fmt = "({})"
        components = (format(c, format_spec) for c in coordinates)
        return outer_fmt.format(", ".join(components))

    def __bytes__(self):
        return (
            bytes([ord(Vector.typecode)]) +
            bytes(self._components)
        )

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v1 = Vector([3, 4, 5, 6, 7, 8, 9, 10])
    print(hash(v1))
    print(len(v1))
    print(v1)
    print(repr(v1))
    print(v1[0], v1[-1], v1[3])
    print(v1[1:4])
    print(v1[-1:])
    v2 = Vector([3, 4, 5, 6, 7, 8, 9, 11])
    print(v1 == v2)
    v3 = Vector([1])
    v4 = Vector([1])
    print(v3 == v4)
    print(v2 == v4)
    print(-v2)
    v5 = Vector([1, 2])
    print(v5)
    v6 = + v5
    print(v6)
    print(v5 is v6)
    print(v1 + v5)

    va = Vector([1, 2, 3])
    vz = Vector([5, 6, 7])
    print(va == Vector(range(1, 4)))
    print(va @ vz)

    print([10, 20, 30] @ vz)
    print([10, 20] @ vz)
    print(vz @ 3)