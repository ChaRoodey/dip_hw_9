from functools import wraps

def how_are_you(func):
    @wraps(func)
    def wrapper():
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию')
        result = func()
        return result
    return wrapper()


@how_are_you
def test():
    print('<Тут что-то происходит>')


if __name__ == '__name__':
    test()