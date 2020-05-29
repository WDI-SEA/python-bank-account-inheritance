class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance
        self.interest = 1.02
    def withdraw(self, amount):
        if self.balance > amount:
           self.balance -= amount
    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} deposited. Balance: {self.balance}')
    def accumulate_interest(self):
        self.balance += (self.balance*self.interest)


class ChildrensAccount(BankAccount):
    def __init__(self, balance = 0):
        self.balance = balance
        self.interest = 0
    def accumulate_interest(self):
        self.balance += 10

class OverdraftAccount(BankAccount):
    def __init__(self, balance = 0):
        self.balance = balance
        self.overdraft = 40
        self.interest = 0

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance = self.balance - self.overdraft
            print(f'False, {self.balance}')
        else:
            self.balance -= amount
            print(f'Ok, {self.balance}')


basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
