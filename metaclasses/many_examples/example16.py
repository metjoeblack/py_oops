

from inspect import Signature, Parameter


def make_signatures(*arg_names: str) -> Signature:
    """
    parms = [
        Parameter('x', Parameter.POSITIONAL_ONLY),
        Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
        Parameter('z', Parameter.KEYWORD_ONLY, default=None),
    ]
    sig = Signature(parms)
    print(type(sig))
    print(sig)
    """
    params = [
        Parameter(arg_name, Parameter.POSITIONAL_OR_KEYWORD)
        for arg_name in arg_names
    ]
    return Signature(params)


class Structure:
    __signature__ = make_signatures()

    def __init__(self, *args, **kwargs) -> None:
        bound_values = self.__signature__.bind(*args, **kwargs)
        for arg_name, arg_value in bound_values.arguments.items():
            setattr(self, arg_name, arg_value)

    def __repr__(self):
        fields = ", ".join(
            f"{attr}={attr_val!r}" for attr, attr_val in vars(self).items()
        )
        return (
            f"{self.__class__.__name__}"
            f"({fields})"
        )


class Stock(Structure):
    __signature__ = make_signatures("name", "shares", "price")


class Point(Structure):
    __signature__ = make_signatures('x', 'y')


if __name__ == '__main__':
    s1 = Stock("Google", 100, 490.1)
    print(s1)
    s2 = Stock("Google", 100, price=521.2)
    print(s2)





