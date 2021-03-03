class BankAccount():
  # Init
  def __init__(self, balance=0):
    # Balance
    self.balance = balance
    # Interest rate - default to .02
    self.interest = .02

  # Deposit
  def deposit(self, amount):
    # Check if negative
    if amount <= 0:
      # Return false
      return False
    # Add amount to balance
    self.balance += amount
    # Return new balance
    return self.balance

  # Withdraw
  def withdraw(self, amount):
    # Check if negative
    if amount <= 0:
      # Return false
      return False
    # Remove amount from balance
    self.balance -= amount
    # Return new balance
    return self.balance

  # accumulate_interest
  def accumulate_interest(self):
    # balance + balance * interest
    self.balance = self.balance + (self.balance * self.interest)
    # Return balance
    return self.balance

# Child account (Inherit from BankAccount)
class ChildrensAccount(BankAccount):
  # Init (BankAccount)
  def __init__(self, balance=0):
    # set super
    super().__init__(balance)
    # set interest rate to 0
    self.interest = 0

  # accumulate_interest
  def accumulate_interest(self):
    # Balance = balance + 10
    self.balance += 10
    return self.balance

# Overdraft (Inherit BankAccount)
class OverdraftAccount(BankAccount):
  # Init (BankAccount)
  def __init__(self, balance=0):
    super().__init__(balance)
    # Overdraft penalty = 20
    self.overdraft_penalty = 20

  # Withdraw
  def withdraw(self, amount):
    # Checks if the amount is more than in the account
    if amount > self.balance:
      self.balance -= self.overdraft_penalty
      return False
    else:
      super().withdraw(amount)

  # accumulate_interest
  def accumulate_interest(self):
    # Does not run interest if amount is 0 or less
    if self.balance <= 0:
      return False
    else:
      super().accumulate_interest()

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
