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


#Example of incapsulation

# Python program to
# demonstrate private members
 
# Creating a Base class
class Base:
    def __init__(self):
        self.a = "Pandorax"
        self.__c = "Cybersecurity"
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
         
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
# Driver code
obj1 = Base()
print(obj1.a) # Prints public 
print(obj1.c) # Causing attribute error, because protected and can't be accessed from derived class



# Python program to
# demonstrate protected members
 
# Creating a base class
class Base:
    def __init__(self):
         
        # Protected member
        self._a = 2
 
# Creating a derived class   
class Derived(Base):
    def __init__(self):
         
        # Calling constructor of
        # Base class
        Base.__init__(self)
        #print("Calling protected member of base class: ")
        #print(self._a)
 
obj1 = Derived()

obj2 = Base()
 
print(obj2.a) # will cause error
 
