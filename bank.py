class BankAccount:
  def __init__(self):
    self.balance = 0
  def deposit(self,amount):
    if amount > 0:
      self.balance += amount
      # self.accumulate_interest()
      return self.balance
    else: 
      return "You can\'t add negative number"
  def withdraw(self,amount):
    if amount > 0 :
      self.balance -= amount
      # accumulate_interest()
      return self.balance
    else:
      return "You can\'t use negative amount"
  def accumulate_interest(self):
    self.balance += (2 * self.balance) / 100
  

class ChildrensAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.intrast = 0
  def accumulate_interest(self):
    self.balance += 10


class OverdraftAccount(BankAccount):
    def __init__(self):
      super().__init__()
      self.overdraft_penalty = 40
    def deposit(self,amount):
      if amount > 0:
        self.balance += amount
        return self.balance
      else:
        return "You can\'t use negative amount"
    def withdraw(self,amount):
      if amount > 0 :
        if self.balance > amount :
          self.balance -= amount
        else:
          self.balance -= self.overdraft_penalty
        return self.balance
      else:
        return "You can\'t use negative amount"
    def accumulate_interest(self):
      if self.balance > 0 :
        super().accumulate_interest()



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
