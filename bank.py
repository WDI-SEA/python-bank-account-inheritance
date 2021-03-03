class BankAccount:
  def __init__(self):
    # variable balance
    self.balance = 0
    # variable interest
    self.interest_rate = .02

    # function deposit
  def deposit(self, amount):
    # check that the amount is positive
    if (amount < 0):
      print('False')
    else:
      self.balance = self.balance + amount

  # function withdrawl
  def withdraw(self, amount):
    # check that the amount is positive
    if (amount < 0):
      print('False')
    else:
      self.balance = self.balance - amount

# function adding interest in
  def accumulate_interest(self):
    # take the balance and multiply by 1.02
    self.balance = self.balance + (self.balance * self.interest_rate)


class ChildrensAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.interest_rate = 10

  def deposit(self, amount):
    super().deposit(amount)

  def withdraw(self, amount):
    super().withdraw(amount)

  def accumulate_interest(self):
    self.balance = self.balance + self.interest_rate


class OverdraftAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.overdraft_penalty = 40

  def deposit(self, amount):
    super().deposit(amount)

  def withdraw(self, amount):
    if(amount>self.balance):
      self.balance = self.balance - self.overdraft_penalty
      print('Tried to overdraft account')

  def accumulate_interest(self):
    if (self.balance <0):
      self.interest_rate == 0
      return
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
