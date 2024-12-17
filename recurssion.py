def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=3
result=fact(n)
print(result)
