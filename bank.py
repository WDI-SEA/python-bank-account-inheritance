class BankAccount:
  def __init__(self, balance=0, interest_rate=0.02 ):
    self.balance = balance
    self.interest_rate = interest_rate
  
  def deposit(self, amount):
    if amount < 0:
      return False
    self.balance = self.balance + amount

  def withdraw(self, amount):
    # the withdraw method returns the amount of money that was successfully withdrawn./
    # these instructions suggest returning the number that i just put into the function.  I'm going to assume that's wrong.
    if amount < 0:
      return False
    self.balance = self.balance - amount
    return self.balance
    
  
  def accumulate_interest(self):
    self.balance = self.balance + (self.balance * self.interest_rate)
    return self.balance
    

basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()


class ChildrensAccount(BankAccount):
  def __init__(self, balance=0):
    super().__init__(balance, 0)

  def accumulate_interest(self):
    self.balance = self.balance + 10
    return self.balance

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

class OverdraftAccount(BankAccount):
   def __init__(self, overdraft_penalty=40, balance=0,interest_rate=.02 ):
    self.balance = balance
    self.overdraft_penalty = overdraft_penalty
    super().__init__(balance, interest_rate)
    if self.balance <= 0:
      self.interest_rate = 0
    if self.balance > 0:
      self.interest_rate = .02
  def withdraw(self, amount):
   
    if amount > self.balance:
      self.balance = self.balance - self.overdraft_penalty
      return False
    self.balance = self.balance - amount
    return self.balance
    pass
    
overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))