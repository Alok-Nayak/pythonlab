# Update attributes of another object
# Goal: Understand that methods can change someone else’s attributes.

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
 
    def deposit(self, amount):
        self.balance += amount

    def transfer(self, other_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount

acc1 = BankAccount("tom")
acc2 = BankAccount("jerry")

acc1.deposit(100)
print(acc1.balance, acc2.balance)

acc1.transfer(acc2, 30)
print(acc1.balance, acc2.balance)
