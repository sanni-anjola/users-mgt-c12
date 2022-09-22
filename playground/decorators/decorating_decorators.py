import functools
import time


def decorate(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        print("I am a before decorator")
        f = func(*args, **kwargs)
        print("I am after decorator")
        return f

    return wrap


def performance_counter(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"the function {f.__name__} took {end - start} to run")
        return func

    return wrapper


@decorate
def hello(name):
    return f"Hello {name}"


@performance_counter
@decorate
def add(x, y):
    """
    adds two numbers
    """
    return x + y


# hello = decorate(hello)
print(hello("Banke"))
print(add(2, 3))

print(add.__name__)
print(add.__doc__)


def multiply(a, b):
    return a * b


multiply_by_5 = functools.partial(multiply, 5)

print(multiply_by_5(6))
