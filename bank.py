class BankAccount:
    def __init__ (self, balance=0):
        self.balance = balance

    def deposit(amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(amount):
        self.balance = self.balance - amount
        return self.balance
    def accumulate_interest():
        self.balance = self.balance * .01
        return self.balance
    pass
class ChildrensAccount(BankAccount):
    def __init__ (self, balance=0):
        super(self).__init__(self, balance=0)
    pass


class OverdraftAccount(BankAccount):
    def __init__ (self, balance=0):
        super(self).__init__(self, balance=0)
    pass


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
