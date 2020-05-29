####################

class BankAccount:
  def __init__(self, balance=0, accountInterest=0.02):
    self.balance = balance
    self.accountInterest = accountInterest

  def deposit(self, deposit):
    self.balance += deposit
  
  def withdraw(self, withdraw):
    if withdraw < 0:
      return False
    self.balance -= withdraw
    return self.balance

  def accumulate_interest(self):
    self.balance = self.balance + (self.balance * self.accountInterest)
    return self.balance

####################

class ChildAccount(BankAccount):
  def __init__(self, balance):
    super().__init__(balance)
    self.accountInterest = 0
    self.balance = balance

  def accumulate_interest(self):
    self.balance = self.balance + 10
    return self.balance

####################

class OverdraftAccount(BankAccount):
  def __init__(self):  
    super().__init__(balance = 0)
    self.overdraft_penalty = 40

  def withdraw(self, amount):
    if amount < 0:
        return False
    if amount > self.balance:
      self.balance = self.balance - self.overdraft_penalty
      return self.balance

  def accumulate_interest(self):
    if self.balance < 0:
        return False
    self.balance = self.balance + (self.balance * self.interest_rate)
    return self.balance


####################

basic_account = BankAccount()
# will_accounts = BankAccount()
basic_account.deposit(600)
print(basic_account.balance)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildAccount(34)
print(f"this is the child's account: {childs_account.balance}, interest: {childs_account.accountInterest}")
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
