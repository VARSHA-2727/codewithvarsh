class solution:
    def pair_of_sums(self,num,target):
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                if num[i]+num[j]==target:
                    return[i,j]
        
