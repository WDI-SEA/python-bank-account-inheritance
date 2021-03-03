class BankAccount():
      def __init__(self, balance=0):
            self.balance = balance
        # self.basic_account = basic_account

  

      def deposit(self, amount):
            self.balance += amount
            print("My basic account has {}".format(self.balance))

      def withdraw(self, amount):
            self.balance -= amount
            print("My basic account has {}".format(self.balance))

      def accumulate_interest(self):
            self.balance = int(self.balance) + (int(self.balance) * .02)


class ChildrensAccount(BankAccount):
      def __init__(self, balance=0):
        self.balance = balance

      def deposit(self, amount):
            self.balance += amount
            print("My childs account has {}".format(self.balance))

      def withdraw(self, amount):
            self.balance -= amount
            print("My childs account has {}".format(self.balance))

      def accumulate_interest(self):
            self.balance += 10

class OverdraftAccount:
      def __init__(self, balance=0):
            self.balance = balance
            self.overdraft_penalty = 40

      def deposit(self, amount):
            self.balance += amount

      def withdraw(self, amount):
            if(self.balance <=amount):
                 
                  self.balance -= self.overdraft_penalty
           

      def accumulate_interest(self):
            if(self.balance >= 0):
                  self.balance += 10



basic_account = BankAccount()
basic_account.deposit(600)
print("Thanks for checking my homework! Basic account has ${}".format(basic_account.balance))
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
