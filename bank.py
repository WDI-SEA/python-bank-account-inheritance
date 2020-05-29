class BankAccount:
  interest = .02
  def __init__(self, balance = 0):
    self.balance = balance

  def deposit(self, amount):
    if amount < 0:
      #make the the transaction for the amount
      return False
    else:
        self.balance = self.balance + amount
        return self.balance 

  def withdraw(self, amount):
    if amount > self.balance or amount < 0:
      return False
    else:
        self.balance = self.balance - amount
        return self.balance 

  def accumulate_interest(self):
    self.balance = self.balance + self.balance * BankAccount.interest
    return self.balance
    # Probably will be using the int() method
    # balance + balance*.02

class ChildrensAccount(BankAccount):
  interest = 0
  def accumulate_interest(self):
    self.balance = self.balance + 10
    return self.balance  

class OverdraftAccount(BankAccount):
  def __init__(self, balance = 0, overdraft_penalty = 40):
    self.balance = balance
    self.overdraft_penalty = overdraft_penalty

  def withdraw(self, amount):
    if amount > self.balance:
      self.balance = self.balance - self.overdraft_penalty
      return False
      
  def accumulate_interest(self):
    if self.balance < 0:
      return self.balance
    else:
      self.balance = self.balance + self.balance * BankAccount.interest
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