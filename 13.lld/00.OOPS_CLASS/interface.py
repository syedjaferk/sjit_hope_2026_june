from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund(self, transaction_id):
        pass

class RazorpayGateway(PaymentGateway):

    def process_payment(self, amount):
        # step 1
        # step 2
        # step 3
        print(f"Processing {amount} using RazorpayGateway")

    def refund(self, transaction_id):
        print(f"Refunding transaction_id {transaction_id} via RazorpayGateway")

class StripeGateway(PaymentGateway):

    def process_payment(self, amount):
        print(f"Processing {amount} using StripeGateway")

    def refund(self, transaction_id):
        print(f"Refunding transaction_id {transaction_id} via StripeGateway")

class PaymentService:

    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway

    def make_payment(self, amount):
        self.gateway.process_payment(amount)

    def make_refund(self, transaction_id):
        self.gateway.refund(transaction_id)


gateway = RazorpayGateway()
service = PaymentService(gateway)
service.make_payment(1000)
