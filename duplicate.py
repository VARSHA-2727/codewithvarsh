class solution:
    def duplicate(self,num):
        num.sort()
        for i in range(1,len(num)):
            if num[i]==num[i-1]:
                return True
        return False
num=[1,2,3,4,5,4]
sol=solution()
print(sol.duplicate(num))
