class Purse:

    def __init__(self, currency):
        self.balance = balance
        self.currency = currency

    def __del__(self):
        return self.balance

    def put_balance(self, amount):
        self.balance = self.balance + amount

    def substract_balance(self, amount):
        self.balance = self.balance - amount

    def print_balance(self):
        print(self.balance)

