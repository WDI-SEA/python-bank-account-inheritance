class BankAccount:
  def __init__(self):
    # balance
    self.balance = 0
    # default intereste rate of 2%
    self.interest_rate = 0.02
    # deposit - returns the balance of the account after adding the deposited amount
  def deposit(self, transaction):
    self.balance += transaction
    return self.balance
    # withdraw - returns the balance after money was successfully withdrawn
  def withdraw(self, transaction):
    # Account returns false if someone withdraw more than balance
    if (self.balance - transaction >= 0):
      self.balance -= transaction
      return self.balance
    else:
      return "You need more money to do this"
    # has accumulate interested method, balance = balance + interest rate earned
  def accumulate_interest(self):
    self.balance = self.balance + (self.balance * self.interest_rate)
    return self.balance

class ChildrensAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.interest_rate = 0
  
    # $10 added to the account if accumulate interest is queued (no interest)
  def accumulate_interest(self):
    self.balance += 10
    return self.balance

class OverdraftAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.penalty = 40
    # has a penalty to user when trying to withdraw more than balance, penalty = $40
  def withdraw(self, transaction):
    if (self.balance - transaction >= 0):
      self.balance -= transaction
      return self.balance
    else:
    # if above happends, withdraw is being canceled, and apply penalty to the balance
      self.balance -= self.penalty
      return self.balance
    # no interest if the balance is negative number
  def accumulate_interest(self):
    if (self.balance > 0):
      self.balance = self.balance + (self.balance * self.interest_rate)
      return self.balance
    else:
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
