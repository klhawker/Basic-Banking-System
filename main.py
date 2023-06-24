class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender", self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def withdrawal(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available: ", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated: ", self.balance)
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Account balance has been updated: ", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance has been updated: ", self.balance)
    
    
