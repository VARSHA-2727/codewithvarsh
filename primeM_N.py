class Solution:
    def primeRange(self, M, N):
        primes = []
        for i in range(M,N+1):
            if i<2:
                continue
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    break
            else:
                primes.append(i)
        return primes
