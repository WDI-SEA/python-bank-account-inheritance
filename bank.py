class BankAccount():
  def __init__(self):
    self.balance = 0
    self.interest = 0.02

  def __str__(self):
    return("Basic account has ${}".format(self.balance))

  def deposit(self,value):
    if value<0:
      return False
    else:
      self.balance = self.balance + value
      return self.balance
  
  def withdraw(self,value):
    if value<0:
      return False
    else:
      self.balance = self.balance - value
      return self.balance

  def accumulate_interest(self):
    self.balance = (1+self.interest)*self.balance
    return self.balance



class ChildrensAccount(BankAccount):
  def __init__(self):
    super().__init__() # runs parent constructor
    self.interest = 0.02

  def accumulate_interest(self):
    self.balance = self.balance +10
    return self.balance

  

class OverdraftAccount(BankAccount):
  def __init__(self):
    super().__init__() # runs parent constructor
    self.overdraft_renality = 40

  def withdraw(self,value):
    if value > self.balance:
      self.balance = self.balance - 40
      return False
    else:
      self.balance = self.balance - value
      return self.balance

  def accumulate_interest(self):
    if self.balance < 0:
      return self.balance
 

basic_account = BankAccount()
basic_account.deposit(600)
print(basic_account)
basic_account.withdraw(17)
print(basic_account)
basic_account.accumulate_interest()
print(basic_account)
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print(childs_account)
childs_account.withdraw(17)
print(childs_account)
childs_account.accumulate_interest()
print(childs_account)
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print(overdraft_account)
overdraft_account.withdraw(17)
print(overdraft_account)
overdraft_account.accumulate_interest()
print(overdraft_account)
