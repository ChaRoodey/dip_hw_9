from functools import wraps
from typing import Callable, Any


def counter(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        wrapper.count += 1
        print(f'Функцию {func.__name__} вызвали {wrapper.count} раз')
        return result
    wrapper.count = 0
    return wrapper


@counter
def test(name: str) -> str:
    return name


def main():
    print(test('Маша'))
    print(test('Саша'))
    print(test('Еблантий'))


main()