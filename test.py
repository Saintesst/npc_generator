from functools import wraps

def log_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Аргументы: позиционные={args}, именованные={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_args
def multiply(a, b):
    return a * b

multiply(3, b=5)