

import json
from typing import Self, Any
from types import SimpleNamespace
from pathlib import Path
from abc import ABC, abstractmethod
from collections import UserDict


class JsonSerializableMixin:
    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(**json.loads(json_str))

    def as_json(self) -> str:
        return json.dumps(vars(self))


class AppSettings(JsonSerializableMixin, SimpleNamespace):
    def save(self, file_path: str | Path) -> None:
        Path(file_path).write_text(self.as_json(), encoding="utf-8")


class Serializer(ABC):
    @abstractmethod
    def serialize(self, data: Any) -> str:
        pass


def TypedKeyMixin(key_type=object):
    class _TypedKeyMixinHelper:
        def __setitem__(self, key, value):
            if not isinstance(key, key_type):
                raise TypeError(
                    f"key must be {key_type} but given {type(key)}"
                )
            super().__setitem__(key, value)
    return _TypedKeyMixinHelper


def TypedValueMixin(value_type=object):
    class _TypedValueMixinHelper:
        def __setitem__(self, key, value):
            if not isinstance(value, value_type):
                raise TypeError(
                    f"value must be {value_type} but given {type(value)}"
                )
            super().__setitem__(key, value)
    return _TypedValueMixinHelper


class Inventory(TypedKeyMixin(str), TypedValueMixin(int), UserDict):
    key_type = "This attribute has nothing to collide with."


def typed_dict(key_type=object, value_type=object):
    def class_decorator(cls):
        setitem = cls.__setitem__

        def __validate_key_value_type(val, expected_type, key_or_value="key"):
            if not isinstance(val, expected_type):
                raise TypeError(
                    f"{key_or_value} must be {expected_type} "
                    f"but given {type(val)}"
                )

        def __setitem__(self, key, value):
            __validate_key_value_type(key, key_type, key_or_value="key")
            __validate_key_value_type(value, value_type, key_or_value="value")
            return setitem(self, key, value)

        cls.__setitem__ = __setitem__
        return cls

    return class_decorator


@typed_dict(str, int)
class InventoryV3(UserDict):
    key_type = "This attribute has nothing to collide with."



if __name__ == '__main__':
    fruits = InventoryV3()
    fruits["apple"] = 42
    # fruits['banana'.encode("utf-8")] = 3.5
    # fruits["banana"] = 3.5
    fruits["banana"] = 3
    print(vars(fruits))
