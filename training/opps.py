# understanding opps concepts
class Account:
    def __init__(self,n,acn,bal,pin):
        self.name=n
        self.acn=acn
        self.bal=bal
        self.pin=pin
    def __str__(self):
        return f'name:{self.name} acc no:{self.acn} balance:{self.bal}'
    def display_details(self):
        print("name:",self.name)
        print("acc no:",self.acn)
        print("balance:",self.bal)
    def deposit(self):
        m=float(input("enter amount to deposit"))
        self.bal+=m
        print("amount updated")
    def withdraw(self):
        m=float(input("enter amount to withdrawed"))
        if self.bal<m:
            print("insufficient balance")
        else:
            self.bal-=m
            print("amount updated",self)
    def pin_validate(self):
        temp_pin=int(input("enter the pin"))
        return temp_pin==self.pin
A1=Account("krishna",123456,50000,1111)
print("welcome to sbi")
if(A1.pin_validate()):
    print("1.view details 2.withdraw 3.deposit 4.quit")
while(1):
    ch=int(input("enter your choice:"))
    if ch==1:
        A1.display_details()
    elif ch==2:
        A1.withdraw()
    elif ch==3:
        A1.deposit()
    elif ch==4:
        print("thank u")
        break
    else:
        print("invalid details")
        
            
        