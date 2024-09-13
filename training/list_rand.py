import random as r
snacks=["samosa","fries","burger"]
drinks=["coke","milkshake","juice"]
spin_wheel=["car","laptop","phone","bike","wm","no prize"]
ch=input("enter 1 to spin")
if ch==1:
    print("you won a ",r.choice(spin_wheel))
