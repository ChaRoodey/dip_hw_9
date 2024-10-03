from time import sleep
from functools import wraps


def slowdown_2(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(2)
        result = func(*args, **kwargs)
        return result
    return wrapper()


@slowdown_2
def test():
    print('<Тут что-то происходит>')


if __name__ == '__name__':
    test()