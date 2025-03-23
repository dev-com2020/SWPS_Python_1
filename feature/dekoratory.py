def simple_decorator(func):
    def wrapper():
        print("Przed...")
        func()
        print("Po...!")

    return wrapper


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] wywołuje {func.__name__} z argumentami {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Wynik: {result}")
        return result

    return wrapper


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print("Cześć")


@logging_decorator
def add(a, b):
    return a + b


@simple_decorator
def hello():
    print("Hello!")


add(3, 4)
hello()
say_hi()
