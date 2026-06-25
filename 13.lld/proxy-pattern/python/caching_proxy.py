from abc import ABC, abstractmethod


# Interface for the Calculator service
class CalculatorService(ABC):
    @abstractmethod
    def add(self, x, y):
        pass

    @abstractmethod
    def subtract(self, x, y):
        pass


# Real implementation of the Calculator service
class Calculator(CalculatorService):
    def add(self, x, y):
        print("Performing add operation")
        return x + y

    def subtract(self, x, y):
        print("Performing subtract operation")
        return x - y


# Caching Proxy for the Calculator service
class CachingProxy(CalculatorService):
    def __init__(self, real_calculator):
        self._real_calculator = real_calculator  # aggregation
        self._cache = {}

    def add(self, x, y):
        key = f"add:{x}:{y}"
        if key not in self._cache:
            result = self._real_calculator.add(x, y)  # execute
            self._cache[key] = result  # store
            print(f"Caching result for add({x}, {y}): {result}")
        else:
            print(f"Using cached result for add({x}, {y}): {self._cache[key]}")
        return self._cache[key]

    def subtract(self, x, y):
        key = f"subtract:{x}:{y}"
        if key not in self._cache:
            result = self._real_calculator.subtract(x, y)
            self._cache[key] = result
            print(f"Caching result for subtract({x}, {y}): {result}")
        else:
            print(f"Using cached result for subtract({x}, {y}): {self._cache[key]}")
        return self._cache[key]


# Client code
def client_code(calculator):
    result_add1 = calculator.add(10, 5)
    result_add2 = calculator.add(10, 5)  # This should use the cached result
    result_subtract1 = calculator.subtract(20, 7)
    result_subtract2 = calculator.subtract(20, 7)  # This should use the cached result


# Using the Calculator directly
print("Using Calculator:")
real_calculator = Calculator()
client_code(real_calculator)

# Using the CachingProxy to add caching to the Calculator
print("\nUsing CachingProxy:")
caching_proxy = CachingProxy(real_calculator)
client_code(caching_proxy)
