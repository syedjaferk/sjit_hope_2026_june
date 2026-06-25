from abc import ABC, abstractmethod

from strategy_pattern.without_strategy import processor

class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount)
        pass

class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print("Paid ", amount, " using credit_card")

class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid ", amount, " using upi")


class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid ", amount, " using cash")

class PaymentProcessor:

    def __init__(self, strategy: PaymentStrategy) -> None:
        self.strategy = strategy

    def process(self, amount):
        self.strategy.pay(amount)

upi = UPIPayment()
processor = PaymentProcessor(upi)
processor.process(500)
