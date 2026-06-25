class BankAccount:
    def __init__(self) -> None:
        self.__balance = 1000

    def deposit(self, amount):
        # Step 1
        # Step 2
        # Step 3
        self.__balance += amount

    def __get_balance(self):
        return self.__balance


ba = BankAccount()
print(ba.__balance)
