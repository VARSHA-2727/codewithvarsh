
class Solution:
    def evenlyDivides(self, n):
        count=0
        for dig in str(n):
             if dig!=0 and n%int(dig)==0:
                 count+=1
        return count
                 
            
        
