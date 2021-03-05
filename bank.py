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
    


  # def accumulate_interest(self, interest)
  #   self.interest = 100 * int(interest)
  #   self.balance = self.interest * self.balance + self.balance
  #   return self.balance




class ChildrensAccount:
  pass

class OverdraftAccount:
  pass

basic_account = BankAccount(500)
basic_account.deposit(-600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(-500)
print("Basic account has ${}".format(basic_account.balance))
# basic_account.accumulate_interest()
# print("Basic account has ${}".format(basic_account.balance))
# print()

# childs_account = ChildrensAccount()
# childs_account.deposit(34)
# print("Child's account has ${}".format(childs_account.balance))
# childs_account.withdraw(17)
# print("Child's account has ${}".format(childs_account.balance))
# childs_account.accumulate_interest()
# print("Child's account has ${}".format(childs_account.balance))
# print()

# overdraft_account = OverdraftAccount()
# overdraft_account.deposit(12)
# print("Overdraft account has ${}".format(overdraft_account.balance))
# overdraft_account.withdraw(17)
# print("Overdraft account has ${}".format(overdraft_account.balance))
# overdraft_account.accumulate_interest()
# print("Overdraft account has ${}".format(overdraft_account.balance))
