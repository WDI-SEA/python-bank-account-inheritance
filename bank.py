class BankAccount:
  def __init__(self):
    self.balance = 0
    self.interest_rate = .02
  
  def deposit(self, amount):
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    # dissallow negative amounts to be withdraw
    if amount < 0:
      return False
    
    self.balance -= amount
    return self.balance

  def accumulate_interest(self):
    self.balance += self.balance * self.interest_rate
    return self.balance


class ChildrensAccount(BankAccount):
  def __init__(self):
    # invoke the parent's constructor
    super().__init__()
    self.interest_rate = 0

  # override the parent's accumulate interest method
  def accumulate_interest(self):
    self.balance += 10
    return self.balance

class OverdraftAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.overdraft_penaly = 40

  def withdraw(self, amount):
    # test to see if their account will go negetive
    negetive_test = self.balance - amount
    # if their account will fo negeitve, deduct the penalty and return false
    if negetive_test < 0:
      self.balance -= self.overdraft_penaly
      return False
    else:
      # refer to the parent's withdraw method
      # otherwise, let them withdraw
      return super().withdraw(amount)

  def accumulate_interest(self):
    # only give interest if they are in good standing 
    if self.balance < 0:
      return False
    else:
      return super().accumulate_interest()

try:
  basic_account = BankAccount()
  basic_account.deposit(600)
  print("Basic account has ${}".format(basic_account.balance))
  basic_account.withdraw(17)
  print("Basic account has ${}".format(basic_account.balance))
  basic_account.accumulate_interest()
  print("Basic account has ${}".format(basic_account.balance))
except Exception as e:
  print(e)

try:
  childs_account = ChildrensAccount()
  childs_account.deposit(34)
  print("Child's account has ${}".format(childs_account.balance))
  childs_account.withdraw(17)
  print("Child's account has ${}".format(childs_account.balance))
  childs_account.accumulate_interest()
  print("Child's account has ${}".format(childs_account.balance))
except Exception as e:
  print(e)
  

try:
  overdraft_account = OverdraftAccount()
  overdraft_account.deposit(12)
  print("Overdraft account has ${}".format(overdraft_account.balance))
  overdraft_account.withdraw(17)
  print("Overdraft account has ${}".format(overdraft_account.balance))
  overdraft_account.accumulate_interest()
  print("Overdraft account has ${}".format(overdraft_account.balance))
except Exception as e:
  print(e)
