# Program to simaulate bank operations
class Bank:
 def __init__(self,acno,name,balance):
  self.acno=acno
  self.name=name
  self.balance=balance
 def deposit(self,acno,amt):
  if self.acno==acno:
   self.balance+=amt
   print("Amount ",amt," is credited in your account ",acno)
  else:
   print("Account no is not valid")
 def withdraw(self,acno,amt):
  if self.acno==acno:
   if self.balance>=amt:
    self.balance-=amt
    print("Amount ",amt," is debited from your account ",acno)
   else:
    print("Unsufficient Fund")
  else:
   print("Account no is not valid")
 def accountBalance(self,acno):
  if self.acno==acno:
   print("Amount",self.balance,"is available in your account",acno)
  else:
   print("Account no is not valid")
#Now we test the class Bank
acno=int(input("Enter account no. : "))
name=input("Enter Name : ")
balance=int(input("Enter balance : "))
b=Bank(acno,name,balance)
print("Account is created")
ch=0
while ch!=4:
 print("1-->Deposit")
 print("2-->Withdraw")
 print("3-->Balance Enquiry")
 print("4-->Exit")
 ch=int(input())
 if ch==1:
  acno=int(input("Enter your account no : "))
  amt=int(input("Enter amount to deposit : "))
  b.deposit(acno,amt)
 elif ch==2:
  acno=int(input("Enter your account no : "))
  amt=int(input("Enter amount to withdraw : "))
  b.withdraw(acno,amt)
 elif ch==3:
  acno=int(input("Enter your account no : "))
  b.accountBalance(acno)
 elif ch==4:
  pass
