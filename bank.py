class BankAccount:
  def __init__(self):
    self.balance = 0
    self.interest_rate = .02
  
  # Class instance methods
  def deposit(self, amount):
    # return False if amount if less than 0
    if amount < 0: return False
    # add the amount to the current balance
    self.balance += amount
    # return the new balance
    return self.balance
  
  def withdraw(self, amount):
    # return False if amount if less than 0
    if amount < 0: return False
    # subract the amount from the current balance
    self.balance -= amount 
    # return the new balance
    return self.balance

  def accumulate_interest(self):
    # multipy the balance by the interest_rate and sum them
    self.balance += self.balance * self.interest_rate
    # return the new balance
    return self.balance



class ChildrensAccount(BankAccount):
  # override parent class methods
  def accumulate_interest(self):
    # add ten dollars to balance
    self.balance += 10
    # return the new balance
    return self.balance


class OverdraftAccount(BankAccount):
  def __init__(self):
    self.overdraft_penalty = 40
    # invoke super to get the parent class's properties
    super().__init__()

  # override parent class methods
  def withdraw(self, amount):
    # subract amount from balance so it can be checked
    result = self.balance - amount

    # if an overdraft will occur, deduct fee and return False
    if result < 0:
      self.balance -= 40
      return False
    
    # otherwise add to the balance like normal
    super().withdraw(amount)

  def accumulate_interest(self):
    # return if balance is below 0
    if self.balance < 0: return False
    # otherwise acculate interest like normal
    super().accumulate_interest()
  
try:
  basic_account = BankAccount()
  basic_account.deposit(600)
  print("Basic account has ${}".format(basic_account.balance))
  basic_account.withdraw(17)
  print("Basic account has ${}".format(basic_account.balance))
  basic_account.accumulate_interest()
  print("Basic account has ${}".format(basic_account.balance))
  print()
except Exception as e:
  print(e)

try:
  childs_account = ChildrensAccount()
  childs_account.deposit(34)
  print("Child's account has ${}".format(childs_account.balance))
  childs_account.withdraw(17)
  print("Child's account has ${}".format(childs_account.balance))
  childs_account.accumulate_interest()
  print("Child's account has ${}".format(childs_account.balance))
  print()
except Exception as e:
  print(e)
  

try:
  overdraft_account = OverdraftAccount()
  overdraft_account.deposit(12)
  print("Overdraft account has ${}".format(overdraft_account.balance))
  overdraft_account.withdraw(17)
  print("Overdraft account has ${}".format(overdraft_account.balance))
  overdraft_account.accumulate_interest()
  print("Overdraft account has ${}".format(overdraft_account.balance))
except Exception as e:
  print(e)
