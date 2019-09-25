class BankAccount:
  def __init__(self, balance = 0, interest_rate = 0.02):
    self.balance = balance
    self.interest_rate = interest_rate

  def deposit(self, amt):
    if amt <= 0:
      print(f'Deposits must be positive.')
      return False
  
    else:
      self.balance += amt

  def withdraw(self, amt):
    if self.balance - amt <= 0:
      print(f'You cannot withdraw more than {self.balance}.')
      return False
    else:
      self.balance -= amt
      
  def accumulate_interest(self):
    self.balance = self.balance + (self.balance * self.interest_rate)


class ChildrensAccount(BankAccount):
  def __init__(self, balance = 0, interest_rate = 0):
    super().__init__(balance, interest_rate)
  
  def accumulate_interest(self):
    self.balance = self.balance + 10

class OverdraftAccount(BankAccount):
  def __init__(self, balance = 0, interest_rate = 0.02, overdraft_penalty = 40):
    super().__init__(balance, interest_rate)
    self.overdraft_penalty = overdraft_penalty

  def withdraw(self, amt):
    if self.balance - amt <= 0:
      self.balance = self.balance - self.overdraft_penalty
      return False
    else:
      self.balance -= amt

  def accumulate_interest(self):
    if self.balance < 0:
      return False
    else:
      self.balance = self.balance + (self.balance * self.interest_rate)

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
