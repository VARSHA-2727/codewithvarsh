prices={"small":15,"medium":20,"large":25}
toppings={"small":2,"medium":3,"large":3}
size=input("enter the size")
bill=prices[size]
if input("do you want toppings y/n")=="y":
    bill+=toppings[size]
    if input("do u want cheeze y/n")=="y":
        bill+=1
print("final price",bill)
        
