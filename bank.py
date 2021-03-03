class BankAccount():
  #initialize the class 
  def __init__(self, balance):
    self.balance = balance

  #deposit
  def deposit(self, deposit):
    if (deposit >= 0):
      self.balance = self.balance + deposit
    else: 
      return False
  #withdraw
  def withdraw(self, withdraw):
    if (self.balance - withdraw >= 0):
      self.balance = self.balance - withdraw
    else:
      return False

  # #accumulate_interest sets the balance equal to the balance plus the balance times the interest rate
  def accumulate_interest(self):
    self.balance = self.balance * 1.02
    

######################################
class ChildrensAccount(BankAccount):
  def __init__(self, balance):
    self.balance = balance

  def accumulate_interest(self):
    self.balance = self.balance + 10

class OverdraftAccount(BankAccount):
  def __init__(self, balance):
    self.balance = balance
    self.overdraft_penalty = 40


    #withdraw
  def withdraw(self, withdraw):
    if (self.balance - withdraw >= 0):
      self.balance = self.balance - withdraw
    else:
      self.balance = self.balance - self.overdraft_penalty
      print('You have tried withdrawing too much and have to pay a fee')
      return False

  def accumulate_interest(self):
    if (self.balance <= 0):
      self.balance = self.balance 
      print('no interest for you')
    else:
      self.balance = self.balance * 1.02
      print('you collect interest')

basic_account = BankAccount(500)
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount(500)
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount(-5)
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(170)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
