class BankAccount():
  def __init__(self):
    self.balance = 0 ## change to a random?
    self.interest_rate = .02
  
  def get_balance(self):
    print(f'You account balance is {self.balance}')

  def withdraw(self, amount):
    if (amount < 0):
      print('False - Invalid Withdrawl amount, please try again.')
      return False
    else:
      self.balance -= amount
      print(f'You withdrew ${amount} and your balance is {self.balance}')
  
  def deposit(self, amount):
    if (amount < 0):
      print('False - Invalid Deposit amount, please try again.')
      return False
    else:
      self.balance += amount
      print(f"You deoposited ${amount} your remaining balance is {self.balance}")

  def accumulate_interest(self):
    old_balance = self.balance
    self.balance = self.balance + self.balance*self.interest_rate
    print(f"You've accumulated interest and your new account balance is {self.balance} up from {old_balance}")

## - interest rate of zero

class ChildrensAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.interest_rate = 0
  
  def accumulate_interest(self):
    self.balance += 10
    print(f"Congratulations! Your account gained a bonus interest and is now {self.balance}")


## - subtract only overdraft_penalty
class OverdraftAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.overdraft_penalty = 40

  def withdraw(self, amount):
    if (amount > self.balance):
      self.balance -= self.overdraft_penalty
      print(f'You cannot withdraw that amount you have been deducted a fee of {self.overdraft_penalty} and your balance is now {self.balance}')
    else:
      self.balance -= amount
      print(f'Your withdrew {amount} and your balance is now {self.balance}')

  def accumulate_interest(self):
    if (self.balance < 0):
      print('Your acount is negative and you cannot accumulate any interest, deposit more money in order to!')
      return
    else: 
      self.balance = self.balance + self.balance*self.interest_rate
      print(f'Your accumulated interest and your balance is now {self.balance}')



#prints
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
