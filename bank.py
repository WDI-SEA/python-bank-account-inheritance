class BankAccount:
  def __init__(self, balance = 0):
    self.balance = balance
    self.interest_rate = 1.02

  def deposit(self, deposit_amount):
    if deposit_amount < 0:
      return False
      print('Cannot deposit a negative value')
    else:
      self.balance = self.balance + deposit_amount
      return self.balance
  
  def withdraw(self, withdraw_amount):
    if withdraw_amount < 0:
      return False
      print('Cannot withdraw a negative amount')
    # elif 0 > (withdraw_amount - self.balance):
    #   return False
    #   print('Insufficient funds')
    else:
      self.balance = self.balance - withdraw_amount
      return self.balance

  def accumulate_interest(self):
    self.balance = self.balance * self.interest_rate
    return self.balance

class ChildrensAccount(BankAccount):
  def __init__(self, balance = 0):
    # super().__init__(self.balance)
    self.balance = balance
    self.interest_rate = 0

  def accumulate_interest(self):
    self.balance = self.balance + 10
  
class OverdraftAccount(BankAccount):
  def __init__(self, balance = 0):
    self.balance = balance
    self.overdraft_policy = 40
    self.interest_rate = 0
  
  def withdraw(self, withdraw_amount):
    if (self.balance - withdraw_amount) < 0:
      self.balance = self.balance - self.overdraft_policy
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

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
