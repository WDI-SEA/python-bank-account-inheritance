class BankAccount:
  def __init__(self, name):
    self.name = name
    self.balance = 0
    self.deposit = deposit
    self.withdraw = withdraw
    self.interest_rate = .02
    self.accumulate_interest = accumulate_interest

    def deposit(self, balance):
      balance = (f'{balance} + {deposit}')
      print(balance)

    def withdraw(self, balance):
      balance = (f'{balance} - {withdraw}')
      print(balance)
      if withdraw < 0:
        return False

    def accumulate_interest(self, balance, interest_rate):
      balance = (f'{balance} + ({balance} * {self.interest_rate})')
      print(balance)

class ChildrensAccount:
  def __init__(self, name):
    self.name = name
    self.balance = 0
    self.deposit = deposit
    self.withdraw = withdraw
    self.interest_rate = 10
    self.accumulate_interest = accumulate_interest

    def deposit(self, balance):
      balance = (f'{balance} + {deposit}')
      print(balance)

    def withdraw(self, balance):
      balance = (f'{balance} - {withdraw}')
      print(balance)

    def accumulate_interest(self, balance, accumulate_interest):
      balance = (f'{balance} + {self.interest_rate}')
      print(balance)

class OverdraftAccount:
  def __init__(self, name):
    self.name = name
    self.balance = 0
    self.deposit = deposit
    self.overdraft_penalty = 40
    self.withdraw = withdraw
    self.accumulate_interest = accumulate_interest

    def deposit(self, balance, deposit):
      balance = (f'{balance} + {deposit}')
      print(balance)

    def withdraw(self, balance):
      if withdraw < balance:
        balance = (f'{balance} - {self.overdraft_penalty}')
        print(balance)

    def accumulate_interest(self, balance, accumulate_interest):
      balance = (f'{balance}')
      print(balance)

basic_account = BankAccount('basic_account')
basic_account.deposit(600)
print(f"Basic account has ${basic_account.balance}".format(basic_account.balance))
basic_account.withdraw(17)
print(f"Basic account has ${basic_account.balance}".format(basic_account.balance))
basic_account.accumulate_interest()
print(f"Basic account has ${basic_account.balance}".format(basic_account.balance))
print()

childs_account = ChildrensAccount('childs_account')
childs_account.deposit(34)
print(f"Child's account has ${childs_account.balance}".format(childs_account.balance))
childs_account.withdraw(17)
print(f"Child's account has ${childs_account.balance}".format(childs_account.balance))
childs_account.accumulate_interest()
print(f"Child's account has ${childs_account.balance}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount('overdraft_account')
overdraft_account.deposit(12)
print(f"Overdraft account has ${overdraft_account.balance}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print(f"Overdraft account has ${overdraft_account.balance}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print(f"Overdraft account has ${overdraft_account.balance}".format(overdraft_account.balance))
