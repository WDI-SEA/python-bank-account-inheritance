# initialize parent bank account class
  # - bank account takes an initial balance
  # - bank account has default interest rate of 2% 
  # - deposit method - add to balance
  # - withdrawl method - subtract from the balance
    # - within these method only take positive numbers, no negatives and return false if tried
  # -Bank account has accumulate_interest method (bal = balance + balence*interest)

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

## Child Class of childrens account (lol)
## - interest rate of zero
## - accumulate interest adds ten to balance (bal = balence +10)
class ChildrensAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.interest_rate = 0
  
  def accumulate_interest(self):
    self.balance += 10
    print(f"Congratulations! Your account gained a bonus interest and is now {self.balance}")


## Child class of overdraft acc
## - overdraft penalty default to 40 
## - cannot withdraw more money than in acc bal
## - deduct only overdraft_penalty
## Cannot accumulate interest if their balance is below zero
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
## Instantiations:
basic_account = BankAccount()
basic_account.deposit(600)
basic_account.withdraw(200)
basic_account.accumulate_interest()
basic_account.get_balance()

childs_account = ChildrensAccount()
childs_account.deposit(500)
childs_account.get_balance()
childs_account.accumulate_interest()
childs_account.deposit(100)
childs_account.withdraw(50)
childs_account.get_balance()


overdraft_account = OverdraftAccount()
overdraft_account.deposit(15)
overdraft_account.withdraw(160)
overdraft_account.get_balance()
overdraft_account.accumulate_interest()
overdraft_account.deposit(200)
overdraft_account.accumulate_interest()
# overdraft_account = OverdraftAccount()
# overdraft_account.deposit(12)
# print("Overdraft account has ${}".format(overdraft_account.balance))
# overdraft_account.withdraw(17)
# print("Overdraft account has ${}".format(overdraft_account.balance))
# overdraft_account.accumulate_interest()
# print("Overdraft account has ${}".format(overdraft_account.balance))
