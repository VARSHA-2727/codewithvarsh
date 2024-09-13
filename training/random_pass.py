import random as r
# print(chr(r.randrange(65,90)))
# print(chr(r.randrange(97,122)))
# print(chr(r.randrange(4)))
range_sp=r.randrange(1,4)
if range_sp==1:
    print(chr(r.randrange(32,47)))
elif range_sp==2:
    print(chr(r.randrange(58,64)))
elif range_sp==3:
    print(chr(r.randrange(91,96)))   