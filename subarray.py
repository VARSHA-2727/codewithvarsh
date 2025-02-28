class solution:
    def subarry(self,num,target):
        sum=0
        for i in range(len(num)):
            for j in range(i,len(num)):
                if num[i]+num[j]==target:
                    return True
        return False
num=[1,2,3,4,5]
target=7
sol=solution()
print(sol.subarry(num,target))
        
    
