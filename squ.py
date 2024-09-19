class Solution:
    def floorSqrt(self, n): 
        if n==0 or n==1:
            return n
        square=1
        ans=1
        while square<=n:
            ans+=1
            square=ans*ans
        return ans-1
