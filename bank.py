class BankAccount:

	def __init__(self, balance=0):
		self.balance = balance

	def deposit(self, amount):
		self.balance = self.balance + amount

	def withdraw(self, amount):
		if(self.balance < amount):
			print("Sorry, not enough funds")
			return False
		else: 
			self.balance -= amount

	def accumulate_interest(self, rate=.02):
  		self.balance = self.balance + (self.balance * rate)


class ChildrensAccount(BankAccount):
	def __init__(self, balance=0):
		self.balance = balance

	def accumulate_interest(self, added_amount=10):
		self.balance += added_amount 

class OverdraftAccount(BankAccount):
	def __init__(self, balance=0):
		super().__init__(balance)

	def withdraw(self, amount, overdraft_penalty=40):
		if(self.balance < amount):
			self.balance -= overdraft_penalty
			return False
		else: 
			self.balance -= amount

	def accumulate_interest(self, rate=.02):
		if self.balance > 0:
  			self.balance = self.balance + (self.balance * rate)
		else:
			return False




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
