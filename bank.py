class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.apy = 0.2

    def deposit(self, amount):
        if amount <= 0:
            print("False")
            return False
        print("${} deposited".format(amount))
        self.balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            print("False")
            return False
        print("${} withdrawn".format(amount))
        self.balance -= amount
    def accumulate_interest(self):
        yields = self.balance * self.apy
        self.balance *= 1 + self.apy
        print("Your dividends made your account rise by ${0} for an end balance of ${1}".format(yields, self.balance))

class ChildrensAccount(BankAccount):
    def __init__ (self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        super().deposit(amount)

    def withdraw(self, amount):
        super().withdraw(amount)

class OverdraftAccount(BankAccount):
    def __init__ (self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        super().deposit(amount)
        
    def withdraw(self, amount):
        super().withdraw(amount)
        if amount < 0:
          return False

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
