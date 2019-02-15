class BankAccount:
  def __init__(self, balance=0, interest_rate=0.02):
    self.balance = balance
    self.interest_rate = interest_rate

  def deposit(self, amount):
    if amount < 1:
      return False
    self.balance += amount
    return self.balance
  
  def withdraw(self, amount):
    if amount < 1:
      return False
    elif amount > self.balance:
      return f"You cannot withdraw {amount} when your balance is {self.balance}"
    self.balance -= amount
    return amount
  
  def accumulate_interest(self):
    self.balance += self.balance * self.interest_rate
    return self.balance

class ChildrensAccount(BankAccount):
  def __init__(self, balance=0, interest_rate=0):
    super().__init__(balance, interest_rate)

  def accumulate_interest(self):
    self.balance += 10
    return self.balance


class OverdraftAccount(BankAccount):
  def __init__(self, balance=0, interest_rate=0.02, overdraft_penalty=40):
    self.overdraft_penalty = overdraft_penalty
    super().__init__(balance, interest_rate)

  def withdraw(self, amount):
    if amount > self.balance:
      self.balance -= self.overdraft_penalty
      return False
  
  def accumulate_interest(self):
    if self.balance < 0:
      return
    self.balance += self.balance * self.interest_rate
    return self.balance

basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
# Basic account has $600
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
# Basic account has $583
print("Basic account has ${}".format(basic_account.balance))
# Basic account has $594.66
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
# Child's account has $34
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
# Child's account has $17
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
# Child's account has $27
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
# Overdraft account has $12
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
# Overdraft account has $-28
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
# Overdraft account has $-28