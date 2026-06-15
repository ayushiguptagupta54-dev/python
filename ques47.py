# CREATE A CLASS BANK ACCOUNT WITH DEPOSIT AND WITHDRAW METHODS.
class Bankaccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount): 
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrwa:", amount)

        else:
            print("Insufficient balance")

    def show_balance(self):
        print("current balance:", self.balance)

acc = Bankaccount(1000)

acc.deposit(500)
acc.withdraw(300)
acc.show_balance()


