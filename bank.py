class BankAccount:
  def __init__(self, balance):
    self.balance = balance

  def deposit(self, amt):
    self.amt = amt
    if (amt < 0):
      return False
    else:
      self.balance += self.amt
      print(self.balance)
  
  def withdraw(self, amt):
    if (self.amt < 0):
      return False
    else: 
      self.balance -= self.amt
      print(self.balance)

  def accumulate_interest(self):
    self.balance *= 1.02
    return self.balance


class ChildrensAccount(BankAccount):
  def __init__(self, balance = 0):
    super().__init__(balance)

  def accumulate_interest(self):
    self.balance += 10
    return self.balance
 

class OverdraftAccount:
  pass

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

# overdraft_account = OverdraftAccount()
# overdraft_account.deposit(12)
# print("Overdraft account has ${}".format(overdraft_account.balance))
# overdraft_account.withdraw(17)
# print("Overdraft account has ${}".format(overdraft_account.balance))
# overdraft_account.accumulate_interest()
# print("Overdraft account has ${}".format(overdraft_account.balance))
