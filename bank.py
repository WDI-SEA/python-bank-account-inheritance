class BankAccount:
  def __init__(self,balance=0):
    self.balance=balance

  def deposit(self, amount):
    if amount<0:
      return False
    else:
      self.balance=self.balance+amount 

  def withdraw(self, amount):
    if amount<0:
      return False
    else:
      self.balance=self.balance-amount  

  def accumulate_interest(self):
    self.balance=self.balance*1.02

basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))

class ChildrensAccount:
  def __init__(self,balance=0):
    self.balance=balance

  def deposit(self, amount):
    if amount<0:
      return False
    else:
      self.balance=self.balance+amount 

  def withdraw(self, amount):
    if amount<0:
      return False
    else:
      self.balance=self.balance-amount  

  def accumulate_interest(self):
    self.balance=self.balance+10

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()


class OverdraftAccount:
  def __init__(self,balance=0):
    self.balance=balance

  def deposit(self, amount):
    if amount<0:
      return False
    else:
      self.balance=self.balance+amount 

  def withdraw(self, amount, overdraft_penalty=40):
    if amount<0:
      return False
    if amount>self.balance:
      self.balance=self.balance-overdraft_penalty
      return False
    else:
      self.balance=self.balance-amount

  def accumulate_interest(self):
    if self.balance<0:
      self.balance=self.balance
    else:
      self.balance=self.balanc*1.02


overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))