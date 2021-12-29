#parent class : user 
    #holds a details about a user
    #has a function to show user detail

#child class: bank 
    #shows detail about the account balance
    #stores details about the amount
    #allows for deposit withdraw and view balance

class User:             #Parent class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def user_details(self):
        print("Personal Details")
        print("Name ", self.name)
        print("Age", self.age)
        print("Gender", self.gender)

class bank(User):       #child class
    def __init__(self, name, age, gender, amount):
        super().__init__(name, age, gender)
        self.balance = 0
        self. amount = amount

    def deposits(self):
        self.balance = self.balance + self.amount
        print("Account Balance has been Updated : $", self.balance)

    def withdraw(self):
        self.amount = self.amount
        if self.amount > self.balance:
            print("Insuffiecnint Funds | Balance available : $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : $", self.balance)
    def view_balance(self):
        self.user_details()
        print("Your account balance : $", self.amount)

name = input("Enter your name : ")
age = int(input("Enter your age : "))
gender = input("Enter your gender : ")
amount= 0

user1 = User(name, age, gender)
user1 = bank(name, age, gender, amount  )
user_command = input("Press D for deposit, W for withdrawal, V to view your balance : ").upper()

if user_command == "D":
    Deposit = int(input("Enter the amount you want to deposit : "))
    user1.deposits(Deposit)
elif user_command == "W":
    withdrawal = int(input("Enter the amount you want to withdraw : "))
    user1.withdraw(withdrawal)
elif user_command == "V":
    user1.view_balance()

