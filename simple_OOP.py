class Purse():

    def __init__(self, currency):
        self.balance = 0.00
        self.currency = currency

    def __del__(self):
        return self.balance

    def put_balance(self, amount):
        self.balance = self.balance + amount

    def substract_balance(self, amount):
        if self.balance <= amount:
            raise ValueError ("Insufficient funds, try again")
        self.balance = self.balance - amount
        return self.balance

    def print_balance(self):
        print(self.balance)

user_1 = Purse('USD')
user_2 = Purse('USD')
user_1.balance = 100
user_2.balance = 200
user_1.put_balance(300)
#transfering money to another user 
user_1.put_balance(user_2.substract_balance(100))
print(user_1.currency)
print(user_1.balance)
print(user_2.balance)

