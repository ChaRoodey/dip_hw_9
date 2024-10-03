from functools import wraps
from typing import Callable, Any
import timeit


def cache_deco(func: Callable) -> Callable:
    cache = {}
    @wraps(func)
    def wrapper(number) -> Any:
        if number in cache:
            return cache[number]
        result = func(number)
        cache[number] = result
        return result
    return wrapper


@cache_deco
def fibonacchi(num: int) -> int:
    if num <= 1:
        return num
    return fibonacchi(num - 1) + fibonacchi(num - 2)


def main():
    timer1 = timeit.Timer(lambda : fibonacchi(300))
    print(timer1.timeit(number=10000))
    timer2 = timeit.Timer(lambda : fibonacchi(300))
    print(timer2.timeit(number=10000))
    print(fibonacchi(10))
    print(fibonacchi(3))


main()