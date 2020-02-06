class BankAccount:
  interest_rate=.02
  def __init__(self):
    self.balance = 0
  def deposit(self, amount):
    # amount = int(input("Deposit amount?"))
    self.balance += amount
    print(f'{amount} deposited. Balance: {self.balance}')
  def withdraw(self, amount):
    if self.balance > amount:
      self.balance -= amount
  def accumulate_interest(self):
    self.balance += (self.balance*self.interest_rate)

class ChildrensAccount(BankAccount):
  interest_rate=0
  def accumulate_interest(self):
    self.balance += 10
  

class OverdraftAccount(BankAccount):
  overdraft_penalty=40
  def withdraw(self, amount):
    if self.balance < amount:
      self.balance = self.balance - self.overdraft_penalty
      print(f'False, {self.balance}')
    else:
      self.balance -= amount
      print(f'Ok, {self.balance}')
  
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
