

from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    def decorator(func):
        # If in optimizing mode, disable type checking
        if not __debug__:
            return func

        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
        print(bound_types)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)

            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            f"Argument {name} must be {bound_types[name]}."
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorator


@typeassert(int, int)
def func1(x, y):
    return x + y


if __name__ == '__main__':
    print(func1(1, 2))


