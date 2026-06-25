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
        return x + y

    def subtract(self, x, y):
        return x - y

# Logging Proxy for the Calculator service
class LoggingProxy(CalculatorService):
    def __init__(self, real_calculator):
        self._real_calculator = real_calculator

    def _log(self, method, *args):
        print(f"Logging: {method}({args})")

    def add(self, x, y):
        self._log("add", x, y)
        result = self._real_calculator.add(x, y)
        print(f"Result of add operation: {result}")
        return result

    def subtract(self, x, y):
        self._log("subtract", x, y)
        result = self._real_calculator.subtract(x, y)
        print(f"Result of subtract operation: {result}")
        return result

# Client code
def client_code(calculator):
    result_add = calculator.add(10, 5)
    result_subtract = calculator.subtract(20, 7)
    print("add", result_add)
    print("sub", result_subtract)

# Using the Calculator directly
# print("Using Calculator:")
real_calculator = Calculator()
# client_code(real_calculator)

# Using the LoggingProxy to add logging to the Calculator
print("\nUsing LoggingProxy:")
logging_proxy = LoggingProxy(real_calculator)
client_code(logging_proxy)