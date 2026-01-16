# A9Q2
# Question: Create a class to perform basic bank operations like deposit(amount),
#           withdraw(amount) and display details. The attributes of the class are
#           account holder's name, account number, balance amount.
# Name: Satyajeet Nayak
# Appl No: 25C200429

class Bank:
    def __init__(self, name, accno, balance):
        self.name = name
        self.accno = accno
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def display(self):
        print("Name:", self.name)
        print("Account No:", self.accno)
        print("Balance:", self.balance)

obj = Bank("Satyajeet", 12345, 5101)

obj.deposit(1000)
obj.withdraw(2000)
obj.display()
