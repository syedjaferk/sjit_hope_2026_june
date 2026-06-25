class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit_card":
            print("Paid ", amount, " using credit_card")
        elif payment_type == "upi":
            print("Paid ", amount, " using upi")
        elif payment_type == "cash":
            print("Paid ", amount, " using cash")
        else:
            raise ValueError("Unsupported payment type")


processor = PaymentProcessor()
processor.process_payment("upi", 500)
