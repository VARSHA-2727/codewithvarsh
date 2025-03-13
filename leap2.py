n=int(input("enter the year"))
if (n%4==0) or(n%400==0 and n%100!=0):
    print("the year is leap yr")
else:
    print("its not leap yr")
