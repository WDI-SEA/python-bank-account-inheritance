class BankAccount:
  def __init__(self, balance=0):
    self.balance = balance
    print('Your balance is: $', balance)

  def deposit(self, amount):
    if amount < 0:
      return False
    else:
      self.balance = self.balance + amount
    # print('You have deposited: $', amount, '. Your balance is now: $', self.balance)

  def withdraw(self, amount):
    if amount < 0:
      return False
    else:
      self.balance = self.balance - amount
    # print('You have withdrawn: $', amount, '. Your balance is now: $', self.balance)

  def accumulate_interest(self):
    self.balance = self.balance * 1.02

class ChildrensAccount(BankAccount):
  def __init__(self, balance=0):
    self.balance = balance

  def accumulate_interest(self):
    self.balance += 10

class OverdraftAccount(BankAccount):
  def __init__(self, overdraft_penalty = 40, balance = 0):
    self.balance = balance
    self.overdraft_penalty = overdraft_penalty

  def withdraw(self, amount):
    if self.balance - amount < 0:
      self.balance -= self.overdraft_penalty
    else:
      self.balance = self.balance - amount
    
  def accumulate_interest(self):
    if self.balance < 1:
      return self.balance
    else:
      self.balance = self.balance * 1.02


basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
# print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
# print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
