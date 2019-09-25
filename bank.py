class BankAccount():
  def __init__(self, balance, interest=1.02):
    self.balance = int(balance)
    self.interest = interest

  def deposit(self, deposit_amount):
    int(deposit_amount)
    if deposit_amount < 0:
      return False
    else:
      new_balance = self.balance + desposit_amount
      self.balance = new_balance
      return self.balance

  def withdraw(self, withdraw_amount):
    int(withdraw_amount)
    if withdraw_amount < 0:
      return False
    else:
      new_balance = self.balance - withdraw_amount
      self.balance = new_balance
      return self.balance
    
  def accumulate_interest(self):
    balance_with_interest = self.balance + (self.balance * self.interest)
    self.balance = balance_with_interset
    return self.balance

class ChildrensAccount(BankAccount):
  def __init__(self, balance=0):
    super().__init__(rate=0)

  def accumulate_interest(self):
    self.balance = self.balance + 10
    return self.balance

class OverdraftAccount(BankAccount):
  def __init__(self, balance=0, overdraft_penatly=-40):
    super().__init__()
    self.overdraft_penalty = overdraft_penalty

  def withdraw(self, amount):
    if amount > self.balance:
      self.balance = self.balance + self.overdraft_penalty
      return False
    else:
      super().withdraw(amount)
      return True
  def accumulate_interest(self):
    if self.balance < 0:
      print("You don't even have enough money to accumulate interest 😥")
    

basic_account = BankAccount(600)
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
