class Solution:
    def floorSqrt(self, n,i=1): 
        if i*i>n:
             return i-1
        return self.floorSqrt(n,i+1)
            
