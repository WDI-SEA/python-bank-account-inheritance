class BankAccount:
    def __init__(self, bal=0, ir=0.02):
        self.balance = bal
        self.apy = ir
    def get_bal(self):
        return self.balance
    def deposit(self, amt):
        if amt <= 0:
            print("returning False")
            return False
        print("${} deposited".format(amt))
        self.balance += amt
    def withdraw(self, amt):
        if amt <= 0:
            print("returning False")
            return False
        print("${} withdrawn".format(amt))
        self.balance -= amt
    def accumulate_interest(self):
        yields = self.balance * self.apy
        self.balance *= 1 + self.apy
        print("The financial year has come to an end. Your dividends made your account rise by ${0} for an end balance of ${1}".format(yields, self.balance))

class ChildrensAccount(BankAccount):
    def __init__ (self, bal=0):
        super().__init__(bal, 0)

    def deposit(self, amt):
        super().deposit(amt)

    def withdraw(self, amt):
        super().withdraw(amt)

class OverdraftAccount:
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
# childs_account.deposit(34)
# print("Child's account has ${}".format(childs_account.balance))
# childs_account.withdraw(17)
# print("Child's account has ${}".format(childs_account.balance))
# childs_account.accumulate_interest()
# print("Child's account has ${}".format(childs_account.balance))
# print()
#
# overdraft_account = OverdraftAccount()
# overdraft_account.deposit(12)
# print("Overdraft account has ${}".format(overdraft_account.balance))
# overdraft_account.withdraw(17)
# print("Overdraft account has ${}".format(overdraft_account.balance))
# overdraft_account.accumulate_interest()
# print("Overdraft account has ${}".format(overdraft_account.balance))
