class BankAccount():
  
  def __init__(self, balance=0, interest_rate=0.02, overdraft_penalty=0):
    self.balance = balance
    self.interest_rate = interest_rate
    self.overdraft_penalty = overdraft_penalty

  def __str__(self):
    return 'This account has a balance of ${}.'.format(self.balance)

  def deposit(self, amount):
    if amount < 0:
      print('Error. Cannot deposit negative amount. Perhaps you wish to make a withdrawal?')
    else:
      self.balance = self.balance + amount
      print(f'${amount} successfully deposited into account. Your new balance is ${self.balance}.')

  def withdraw(self, amount):
    if amount < 0:
        print('Error. Cannot withdraw negative amount. Perhaps you wish to make a deposit?')
    elif self.overdraft_penalty == 0:
      self.balance = self.balance - amount
      print(f'${amount} successfully withdrawn from account. Your new balance is ${self.balance}')
    else: 
      if amount > self.balance:
        self.balance = self.balance - self.overdraft_penalty
        print(f'Unable to process. Requested amount exceeds account balance. A penalty of ${self.overdraft_penalty} has been applied to your account. Your new balance is ${self.balance}.')
      else:
        self.balance = self.balance - amount
        print(f'${amount} successfully withdrawn from account. Your new balance is ${self.balance}')

  def accumulate_interest(self):
    if self.interest_rate == 0:
      self.balance = self.balance + 10
      print(f'$10 added to account. Your new balance is ${self.balance}.')
    elif self.overdraft_penalty > 0 and self.balance < 0:
      print('Error. Interest accumulation not applicable to negative balance.')
    else:
      self.balance = self.balance + (self.balance * self.interest_rate)
      print(f'Interest accumulated. Your new balance is ${self.balance}.')
    
class ChildrensAccount(BankAccount):
  def __init__(self, balance=0, interest_rate=0, overdraft_penalty=0):
    super().__init__(balance, interest_rate, overdraft_penalty)
  
class OverdraftAccount(BankAccount):
  def __init__(self, balance=0, interest_rate=0.02, overdraft_penalty=40):
    super().__init__(balance, interest_rate, overdraft_penalty)

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