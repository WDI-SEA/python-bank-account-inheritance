class BankAccount:
  def __init__(self, name):
    self.name = name
    self.balance = 0
    self.interest = 1.02

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
  def withdraw(self, amount):
    if amount > 0:
      if amount <= self.balance:
        self.balance -= amount
      else:
        print('You don\'t have that much damn money.')
  def accumulate_interest(self):
    self.balance *= self.interest

class ChildrensAccount:
  def __init__(self, name):
    self.name = name
    self.balance = 0
    self.interest = 1.00

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
  def withdraw(self, amount):
    if amount > 0:
      if amount <= self.balance:
        self.balance -= amount
      else:
        print('You don\'t have that much money.')
  def accumulate_interest(self):
    self.balance += 10

class OverdraftAccount:
  def __init__(self, name):
    self.name = name
    self.balance = 0
    self.interest = 1.12
    self.penalty = 40

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
  def withdraw(self, amount):
    if amount > 0:
      if amount <= self.balance:
        self.balance -= amount
      else:
        self.balance -= self.penalty
  def accumulate_interest(self):
    if self.balance > 0:
      self.balance *= self.interest

  

basic_account = BankAccount('basic_account')
basic_account.deposit(600)
print(f"Basic account has ${basic_account.balance}".format(basic_account.balance))
basic_account.withdraw(17)
print(f"Basic account has ${basic_account.balance}".format(basic_account.balance))
basic_account.accumulate_interest()
print(f"Basic account has ${basic_account.balance}".format(basic_account.balance))
print()

childs_account = ChildrensAccount('childs_account')
childs_account.deposit(34)
print(f"Child's account has ${childs_account.balance}".format(childs_account.balance))
childs_account.withdraw(17)
print(f"Child's account has ${childs_account.balance}".format(childs_account.balance))
childs_account.accumulate_interest()
print(f"Child's account has ${childs_account.balance}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount('overdraft_account')
overdraft_account.deposit(12)
print(f"Overdraft account has ${overdraft_account.balance}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print(f"Overdraft account has ${overdraft_account.balance}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print(f"Overdraft account has ${overdraft_account.balance}".format(overdraft_account.balance))
