import math
class BankAccount:
  # pass
  def __init__(self, balance):
    self.balance = balance

  def deposit(self, deposit):
    if deposit <= 0:
      print("Cannot do that!")
      return False
    else:
      self.deposit = deposit
      self.balance = deposit + self.balance
      return self.balance


  def withdraw(self, withdraw):
    if withdraw <= 0:
      print("Cannot do that!")
      return False
    else:
      self.withdraw = withdraw
      self.balance = self.balance - withdraw
      return self.balance
    


  def accumulate_interest(self, interest):
    self.interest = interest / 100
    self.balance = (self.interest * self.balance) + self.balance
    return math.floor(int(self.balance))

class ChildrensAccount(BankAccount):
  def __init__(self, balance):
    super().__init__(balance)

  def accumulate_interest(self, money):
    self.money = money
    self.balance = self.balance + 10
    return self.balance

class OverdraftAccount(BankAccount):
  def __init__(self, balance):
    super().__init__(balance)

  def withdraw(self, withdraw):
    self.withdraw = withdraw
    self.overdraft_penalty = 40
    if (self.balance - withdraw < 0):
      self.balance = self.balance - self.overdraft_penalty
      print("False")
      return self.balance
    else:
      self.balance =self.balance - withdraw
      return self.balance

  def accumulate_interest(self, interest):
    if self.balance < 0:
      print("False")
      return self.balance
    else:
      self.interest = interest / 100
      self.balance = (self.interest * self.balance) + self.balance
      return math.floor(int(self.balance))

    

basic_account = BankAccount(583)
basic_account.deposit(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(-17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest(2)
print("Basic account plus interest has ${}".format(basic_account.balance))
# print()

childs_account = ChildrensAccount(0)
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest(58)
print("Child's account has ${}".format(childs_account.balance))
# print()

overdraft_account = OverdraftAccount(0)
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest(3)
print("Overdraft account has ${}".format(overdraft_account.balance))
