class BankAccount:
  def __init__(self):
    self.balance = 0
  def __str__(self):
    return 'This account has a balance of ${}'.format(self.balance)
  def deposit(self, amount):
    self.balance += amount
    print(f'${amount} has been deposited into this account')
# class ChildrensAccount:
#   pass

# class OverdraftAccount:
#   pass

blakes_account = BankAccount()
blakes_account.deposit(30)
print(blakes_account)






















# basic_account = BankAccount()
# basic_account.deposit(600)
# print("Basic account has ${}".format(basic_account.balance))
# basic_account.withdraw(17)
# print("Basic account has ${}".format(basic_account.balance))
# basic_account.accumulate_interest()
# print("Basic account has ${}".format(basic_account.balance))
# print()

# childs_account = ChildrensAccount()
# childs_account.deposit(34)
# print("Child's account has ${}".format(childs_account.balance))
# childs_account.withdraw(17)
# print("Child's account has ${}".format(childs_account.balance))
# childs_account.accumulate_interest()
# print("Child's account has ${}".format(childs_account.balance))
# print()

# overdraft_account = OverdraftAccount()
# overdraft_account.deposit(12)
# print("Overdraft account has ${}".format(overdraft_account.balance))
# overdraft_account.withdraw(17)
# print("Overdraft account has ${}".format(overdraft_account.balance))
# overdraft_account.accumulate_interest()
# print("Overdraft account has ${}".format(overdraft_account.balance))
