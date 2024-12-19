class BankAccount:
  def __init__ (self,account_holder,balance=0):
    self.account_holder=account_holder
    self.balance=balance


  def deposit(self,amount):
    self.balance+= amount
    print(f"Deposited ${amount}.New balance:${self.balance}")

  def withdraw(self,amount):


    if amount>self.balance:
        print(f"insufficient funds! current balance:${self.balance}")
    else:
        self.balance-=amount
        print(f"withdrew ${amount}.New balance:${self.balance}")
account=BankAccount( account_holder= "shivani", balance=100000)
account.deposit(50000)
account.withdraw(30000)
account.withdraw(20000)
