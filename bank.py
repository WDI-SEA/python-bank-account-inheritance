class BankAccount():
  def __init__(self, balance=0):
    self.balance = balance


  def __str__(self):
    return 'Your checking is ${}'.format(self.checking)
  
  def __str__(self):
    return 'Your savings is ${}'.format(self.checking)

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    self.balance -= amount


class ChildrensAccount():
  super().__init__(savings, checking, amount)
 

class OverdraftAccount():
  def withdraw(self, amount):

  


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
