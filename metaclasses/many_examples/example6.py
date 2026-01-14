
from functools import partial, wraps
import logging


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name is not None else func.__module__
    logger = logging.getLogger(logname)
    logmessage = message if message is not None else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.log(level, logmessage)
        return func(*args, **kwargs)
    return wrapper


@logged
def add(a, b):
    return a + b


@logged(level=logging.CRITICAL, name="example")
def spam():
    print("spam")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # print(add(1, 2))
    spam()
