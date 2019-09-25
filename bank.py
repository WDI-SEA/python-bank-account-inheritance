class BankAccount:
  def __init__(self):
    self.balance = 0
    self.interest_rate = .02
  def deposit(self, amt):
    try:
      if int(amt) < 0:
        print("Amount was negative, please fix and retry")
        return False
      self.balance += int(amt)
    except:
      print("Amount was not a number, please fix and retry")
    return self.balance
  def withdraw(self, amt):
    try:
      if int(amt) < 0:
        print("Amount was negative, please fix and retry")
        return False
      if self.balance > int(amt):
        self.balance -= int(amt)
      else:
        print("Insufficient balance, cancelling")
    except:
      print("Amount was not a number, please fix and retry")
    return self.balance
  def accumulate_interest(self):
    self.balance = self.balance * (1 + self.interest_rate)
    return self.balance


class ChildrensAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.interest_rate = 0.0
  def accumulate_interest(self):
    self.balance += 10
    return self.balance


class OverdraftAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.overdraft_penalty = 40
  def withdraw(self, amt):
    try:
      if int(amt) < 0:
        print("Amount was negative, please fix and retry")
        return False
      if self.balance < int(amt):
        print("Overdraft!")
        self.balance -= self.overdraft_penalty
        return False
    except:
      print("Amount was not a number, please fix and retry")
  def accumulate_interest(self):
    if self.balance >= 0:
      self.balance = self.balance * (1 + self.interest_rate)
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
