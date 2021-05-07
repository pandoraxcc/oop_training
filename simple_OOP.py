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

# Python code to demonstrate how parent constructors
# are called.
  
# parent class
class Person( object ):    
  
        # __init__ is known as the constructor         
        def __init__(self, name, idnumber):   
                self.name = name
                self.idnumber = idnumber
        def display(self):
                print(self.name)
                print(self.idnumber)


# example of inheritance
# child class
class Employee( Person ):           
        def __init__(self, name, idnumber, salary, post):
                self.salary = salary
                self.post = post
  
                # invoking the __init__ of the parent class 
                Person.__init__(self, name, idnumber) 
  
                  
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")    
  
# calling a function of the class Person using its instance
a.display() 