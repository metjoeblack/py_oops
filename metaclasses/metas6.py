
from typing import Any, Optional


class OneShotDict(dict):

    def __init__(self, name, existing: Optional[dict[str, Any]] = None) -> None:
        super().__init__()
        self._name = name
        if existing is not None:
            for k, v in existing.items():
                self[k] = v

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(
                f"cannot assign to existing key {key!r} "
                f"in {self._name!r}"
            )
        super().__setitem__(key, value)


class ProhibitDuplicatesMeta(type):

    @classmethod
    def __prepare__(metacls, classname, super_classes, **kwargs):
        return OneShotDict(classname)


class Dodgy(metaclass=ProhibitDuplicatesMeta):

    def __init__(self, name) -> None:
        self.name = name

    def action(self):
        print(f"{self.__class__.__name__} action")

    def action(self, message: str) -> None:
        print(f"{self.__class__.__name__} {message}")


if __name__ == '__main__':
    pass


