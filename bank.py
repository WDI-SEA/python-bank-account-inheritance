class BankAccount():
  def __init__(self, balance=0):
    self.balance = balance
  def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance
  def withdraw(self, amount):
    self.balance = self.balance - amount
    return self.balance
  def accumulate_interest(self):
    self.balance = self.balance + self.balance * .02
    return self.balance

class ChildrensAccount(BankAccount):
  def __init__(self, balance=0):
    BankAccount.__init__(self)
  def accumulate_interest(self):
    self.balance += 10
    return self.balance


class OverdraftAccount(BankAccount):
  def __init__(self, overdraft_penalty = 40):
    self.overdraft_penalty = overdraft_penalty
    BankAccount.__init__(self)
  def withdraw(self, amount):
    if amount > self.balance:
      self.balance -= (self.overdraft_penalty)
      return self.balance
  def accumulate_interest(self):
    if self.balance <= 0:
      return self.balance
    else:
      self.balance = self.balance + self.balance * .02
      return self.balance

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

print("TEST NEGATIVE BALANCE withdrawal $17")
overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))

print()

print("TEST POSITIVE BALANCE withdrawal $10")
overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(10)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
