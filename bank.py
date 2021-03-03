class BankAccount:
  def __init__(self, amount):
    # balance
    self.balance = 0
    self.transaction = amount
    # deposit - returns the balance of the account after adding the deposited amount
    def deposit(self):
      self.balance += self.transaction
    # withdraw - returns the balance after money was successfully withdrawn
    # Account returns false if someone withdraw more than balance
    # default intereste rate of 2%
    # has accumulate interested method, balance = balance + interest rate earned
    
    

class ChildrensAccount:
    # balance
    # $10 added to the account if accumulate interest is queued (no interest)
  pass

class OverdraftAccount:
    # has a penalty to user when trying to withdraw more than balance, penalty = $40
    # if above happends, withdraw is being canceled, and apply penalty to the balance
    # no interest if the balance is negative number
  pass

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
