# Decorator pattern: Logging
def log(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(message)
            print("Function execution started")
            func(*args, **kwargs)
            print("Function execution finished")

        return wrapper

    return decorator


@log("Test Message")
def add(a, b):
    print(a + b)


add(3, 5)
