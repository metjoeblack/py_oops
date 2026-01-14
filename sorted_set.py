

import collections.abc
from typing import Any
import bisect
from itertools import chain


class SortedSet(collections.abc.Sequence):
    
    def __init__(self, items=None) -> None:
        self._items = sorted(set(items)) if items is not None else []
    
    def __repr__(self) -> str:
        return "{0}({1})".format(type(self).__name__, self._items if self._items else "")
    
    def __contains__(self, value):
        try:
            self.index(value=value)
            return True
        except ValueError:
            return False
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        yield from self._items
    
    def __getitem__(self, idx):
        result = self._items[idx]
        return SortedSet(result) if isinstance(idx, slice) else result
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, type(self)):
            return value._items == self._items
        return NotImplemented

    def __add__(self, rhs):
        cls = type(self)
        return cls(chain(self._items, rhs._items)) if isinstance(rhs, cls) else NotImplemented
    
    def __mul__(self, rhs):
        return SortedSet() if rhs <= 0 else self

    def __rmul__(self, lhs):
        return self * lhs
    
    def _is_unique_and_sorted(self):
        return all(self[i] < self[i + 1] for i in range(len(self) - 1) )

    def count(self, value: Any) -> int:
        assert self._is_unique_and_sorted()
        return int(value in self._items)

    def index(self, value):
        assert self._is_unique_and_sorted()
        idx = bisect.bisect_left(self._items, value)
        if idx != len(self._items) and self._items[idx] == value:
            return idx
        raise ValueError(f"value '{value}' not found")

    def issubset(self, iterable):
        return self <= type(self)(iterable)
    
    def intersection(self, iterable):
        return self & type(self)(iterable)



if __name__ == "__main__":
    s = SortedSet([3, 1, 4, 2, 3, 4, 9])
    print(s)
    print(3 in s)
    print(5 not in s)
    print(s.index(4))
    t = SortedSet()
    print(t)
    q = SortedSet([6, 7, 9, 12])
    print(s + q)
    # print(s[1])
    # print(s[1: 3])
    ...