
# Parent Class
class BankAccount:
  def __init__(self, balance = 0):
    self.balance = balance
    self.interest = .02

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
    else:
      return False

  def withdraw(self, amount):
    if amount > 0:
      self.balance -= amount
    else:
      return False
    
  def accumulate_interest(self):
    # It says to return this value?
    self.balance = self.balance + (self.balance * self.interest)


# Child Class
class ChildrensAccount(BankAccount):
  def __init__(self, balance = 0):
    super().__init__()
    self.balance = balance
    self.interest = 0
  
  def accumulate_interest(self):
    self.balance = self.balance + 10
  
class OverdraftAccount(BankAccount):
  def __init__(self, balance = 0):
    super().__init__()
    self.balance = balance
    self.overdraft_penalty = 40
   
  def interest_determination(self):
      # How do I get the self.balance from the parent?
      if self.balance < 0:
          self.interest = 0
      else:
          self.interest = .02

  def withdraw(self, amount):
      if self.balance < amount:
          print(f"Your balance is: {self.balance}")
          self.balance = self.balance - (self.overdraft_penalty + amount)
          print(f"Thank you for using our overdraft service :) You have withdrawn ${amount}. We have charged you a fee of {self.overdraft_penalty}, your current balance is now {self.balance}")
      else:
          self.balance -= amount
          print(f"{amount} has been withdrawn from your account. You now have {self.balance} remaining.")



  

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
