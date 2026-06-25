from abc import ABC, abstractmethod


# Component
class AccountComponent(ABC):
    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def get_statement(self):
        pass


# Leaf
class BankAccount(AccountComponent):
    def __init__(self, account_number, balance, statement):
        self.account_number = account_number
        self.balance = balance
        self.statement = statement

    def get_balance(self):
        return self.balance

    def get_statement(self):
        return f"Account {self.account_number} Statement:\n{self.statement}"


# Composite
class CustomerAccount(AccountComponent):
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_balance(self):
        total_balance = sum(account.get_balance() for account in self.accounts)
        return total_balance

    def get_statement(self):
        consolidated_statement = f"Consolidated Statement for {self.customer_name}:\n"
        for account in self.accounts:
            consolidated_statement += account.get_statement() + "\n"
        return consolidated_statement


# Usage
if __name__ == "__main__":
    account1 = BankAccount("123456", 5000, "Transaction 1: +$100\nTransaction 2: -$50")
    account2 = BankAccount("789012", 7000, "Transaction 1: +$200\nTransaction 2: -$100")

    customer = CustomerAccount("John Doe")
    customer.add_account(account1)
    customer.add_account(account2)

    print("Account 1 balance ", account1.get_balance())

    # Generate Customer’s total account balance
    total_balance = customer.get_balance()
    print(f"Customer's Total Account Balance: ${total_balance}")

    # Generate Consolidated account statement
    consolidated_statement = customer.get_statement()
    print(consolidated_statement)
