# Decorator pattern: Logging
def log(func):
    def wrapper(*args, **kwargs):
        print("Function execution started")
        func()
        print("Function execution finished")

    return wrapper


@log
def do_something():
    print("Doing something")


do_something()
