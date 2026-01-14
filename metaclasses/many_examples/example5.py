
from functools import partial, wraps
import logging


def attach_wrapper(obj, func=None):
    """Utility decorator to attach a function as an attribute of obj."""
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    """
    Add logging to a function. Level is the logging level, name is the logger
    name, and message is the logging message. If name and message are not
    specified, they default to the function's module and name.
    """
    def decorator(func):
        logname = name if name is not None else func.__module__
        logger = logging.getLogger(logname)
        logmessage = message if message is not None else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.log(level, logmessage)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)
        def set_message(new_message):
            nonlocal message
            message = new_message

        return wrapper
    return decorator


@logged(logging.DEBUG)
def add(a, b):
    return a + b


@logged(logging.CRITICAL, "example")
def spam():
    print("spam")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print(add(1, 2))
    spam()

    add.set_message("Add called")
    print(add(2, 3))

    add.set_level(logging.WARNING)
    print(add(3, 4))





