class Order:
    pass


class Customer:
    def __init__(self):
        self.order = Order() # Association.
        self.orders = []
