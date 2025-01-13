class Solution:
    def armstrongNumber (self, n):
        n=str(n)
        length=len(n)
        sum=0
        n=int(n)
        n=n%10
        power=pow(n,length)
        n=n/10
        sum+=int(n)**length
        if(sum==n):
            return True
        else:
            return False
