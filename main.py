def simple_decorator(func):
    def wrapper(name):
        print('Начало')
        func(name)
        print("Конец")
    return wrapper
@simple_decorator
def say_hello(name):
    print(f'Привет, {name}')

say_hello("Алексей")
