overdraft_penalty = 40

class BankAccount():
  def __init__(self, account_balance):
    self.balance = account_balance
    
  def deposit(self, amount):
    self.balance += amount
    
  def withdraw(self, amount):
    if(self.balance < amount):
      global overdraft_penalty
      self.balance -= overdraft_penalty
      return False
    self.balance -= amount
    
  def accumulate_interest(self):
    self.interest = 0.02
    self.balance = self.balance + (self.balance * self.interest)
    

class ChildrensAccount(BankAccount):
  def __init__(self, account_balance):
    super().__init__(account_balance)
  def accumulate_interest(self):
    self.interest = 10
    self.balance += self.interest


class OverdraftAccount(BankAccount):
  def __init__(self, account_balance):
    super().__init__(account_balance)
  def accumulate_interest(self):
    self.interest = 0
    self.balance = self.balance

basic_account = BankAccount(0)
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(601)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
# print()

childs_account = ChildrensAccount(0)
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
# print()

overdraft_account = OverdraftAccount(0)
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
