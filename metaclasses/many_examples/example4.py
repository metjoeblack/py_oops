
from functools import wraps
import logging


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
        return wrapper
    return decorator


@logged(logging.DEBUG, "just for debug")
def add(a, b):
    return a + b


@logged(logging.CRITICAL, "example")
def spam():
    print("spam")


if __name__ == '__main__':
    print(add(1, 2))
    spam()
    pass

