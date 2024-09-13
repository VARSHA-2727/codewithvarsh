import random as r
pw=""
pw=pw+chr(r.randrange(65,90))
pw=pw+chr(r.randrange(48,57))
pw=pw+chr(r.randrange(32,47))
for i in range(5):
    pw+=pw+chr(r.randrange(97,122))
print("random password=",pw)