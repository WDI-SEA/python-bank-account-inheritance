class BankAccount():
  def __init__(self, balance=0):
    self.balance = balance
    self.interest_rate = .02
    # self.accumulate_interest = accumulate_interest

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    if amount > 0:
      self.balance -= amount
    elif amount < 0:
      return False
    elif amount > balance:
       self.balance -= overdraft_penalty  
      
  def accumulate_interest(self):
    self.balance = self.balance + (self.balance * self.interest_rate)
   


class ChildrensAccount(BankAccount):
  def __init__(self, balance=0):
    super().__init__()
    self.balance = balance
    self.interest_rate = 0
   
  
 

class OverdraftAccount(BankAccount):
  def __init__(self, overdraft_penalty=40):
    super().__init__()
   

    
  


basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(20)
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
