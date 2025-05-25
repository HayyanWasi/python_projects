from functools import wraps

def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("function is being called")
        return func(*args, **kwargs)      #*args is used to save tupple positional args and **kwargs used to save dictionary keyword args
    return wrapper

@log_function_call
def say_hello():
    print(f"hello")

say_hello()