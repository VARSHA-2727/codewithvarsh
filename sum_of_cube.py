def cube_sum(n):
    total=0
    for i in range(n):
        total+=i**3
    return total 
n=int(input("enter the n "))
print(cube_sum(n))
