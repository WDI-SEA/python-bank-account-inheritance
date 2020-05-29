class BankAccount:
  def __init__(self, balance=0, interest=0.02):
    self.balance = balance
    self.interest = interest

  def deposit(self, amount):
    if amount < 0:
      return False
    else:
      self.balance = self.balance + amount
      print(f'Deposited ${amount} into account')
      return self.balance

  def withdraw(self, amount):
    if amount < 0:
      print('Can\'t withdraw a negative amount, our bank doesn\'t pay you!')
      return False
    else:
      self.balance = self.balance - amount
      print(f'Withdrew ${amount} from account')
      return self.balance

  def accumulate_interest(self):
    if self.balance > 0:
      self.balance += (self.balance*self.interest)
      print(f'Your account accrued ${self.balance*self.interest} in interest')
      return self.balance
  

class ChildrensAccount(BankAccount):
  def __init__(self, balance=0):
    super().__init__(balance)

  def accumulate_interest(self):
    self.balance += 10
    print(f'Allowance is $10')
    return self.balance


class OverdraftAccount(BankAccount):
  def __init__(self, balance=0, interest=0.02, overdraft_penalty=40):
    super().__init__(balance, interest)
    self.overdraft_penalty = overdraft_penalty
    
  def withdraw(self, amount):
    if amount > self.balance:
      print('Can\'t withdraw more than your balance, now give us $40 for the hassle!')
      self.balance -= self.overdraft_penalty
      print(f'You just lost ${40}!')
      return False
    else:
      self.balance = self.balance - amount
      print(f'Withdrew ${amount} from your account')
      return self.balance

  def accumulate_interest(self): 
    if self.balance < 0:
      print('You don\'t want to accrue negative interest, that would be bad.')
      return self.balance
    else: 
      self.balance += (self.balance*self.interest)
      print(f'Your account accrued ${self.balance*self.interest} in interest')
      return self.balance

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
