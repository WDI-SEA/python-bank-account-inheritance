class BankAccount:
  pass

class ChildrensAccount:
  pass

class OverdraftAccount:
  pass

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

# try:
#   childs_account = ChildrensAccount()
#   childs_account.deposit(34)
#   print("Child's account has ${}".format(childs_account.balance))
#   childs_account.withdraw(17)
#   print("Child's account has ${}".format(childs_account.balance))
#   childs_account.accumulate_interest()
#   print("Child's account has ${}".format(childs_account.balance))
#   print()
# except Exception as e:
#   print(e)
  

# try:
#   overdraft_account = OverdraftAccount()
#   overdraft_account.deposit(12)
#   print("Overdraft account has ${}".format(overdraft_account.balance))
#   overdraft_account.withdraw(17)
#   print("Overdraft account has ${}".format(overdraft_account.balance))
#   overdraft_account.accumulate_interest()
#   print("Overdraft account has ${}".format(overdraft_account.balance))
# except Exception as e:
#   print(e)
