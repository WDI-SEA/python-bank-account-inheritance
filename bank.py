class BankAccount:
  # 'pass' is a line that says to do nothing; it's a placeholder value.
  def __init__(self, interest_rate=0.02):
    self.balance = 0
    self.interest_rate = interest_rate

  def deposit(self, amount):
    if amount < 0:
      print('You cannot withdraw or deposit negative amounts.')
      return False
    self.balance += amount
    print(f'After depositing ${amount}, your new balance is ${self.balance}')
  
  def withdraw(self, amount):
    if amount < 0:
      print('You cannot withdraw or deposit negative amounts.')
      return False
    elif self.balance - amount < 0:
      print(f'You do not have enough in your balance (currently ${self.balance} to withdraw ${amount}')
      return False
    else:
      self.balance -= amount
      print(f'After withdrawing ${amount}, your new balance is ${self.balance}')

  def accumulate_interest(self):
    self.balance *= (1 + self.interest_rate)
    print(f'Your new balance is ${self.balance}')

class ChildrensAccount(BankAccount):
  def __init__(self, interest_rate=0):
    super().__init__(interest_rate)
  
  def accumulate_interest(self):
    self.balance += 10
    print(f'Your new balance is ${self.balance}')

class OverdraftAccount(BankAccount):
  def __init__(self, overdraft_penalty=40):
    super().__init__()
    self.overdraft_penalty = overdraft_penalty

  def withdraw(self, amount):
    if self.balance - amount < 0:
      self.balance -= self.overdraft_penalty
      print(f'You do not have enough in your balance to withdraw ${amount}. You have been charged an overdraft penalty of ${self.overdraft_penalty}, which has been deducted from your account. Your balance is now ${self.balance}')
      return False
    else: 
      self.balance -= amount
      print(f'After withdrawing ${amount}, your new balance is ${self.balance}')
  
  def accumulate_interest(self):
    if (self.balance < 0):
      return

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
