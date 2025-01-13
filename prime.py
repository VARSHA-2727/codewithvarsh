class Solution:
    def isPrime(self, n):
        if n<=1:
            return False
        if n%2==0:
            return False
        for i in range(3,int(n**0.5)+1,2):
            if i%n==0:
                return False
        return True

