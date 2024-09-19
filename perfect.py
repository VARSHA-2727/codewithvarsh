import math

class Solution:
    def isPerfectNumber(self, N):
        if N == 0 or N == 1:
            return 0  # Return 0 for 0 and 1 since they are not perfect numbers
        
        sumofdiv = 1  # Start with 1, which is a proper divisor for any N > 1
        for num in range(2, int(math.sqrt(N)) + 1):
            if N % num == 0:
                sumofdiv += num
                if num != N // num:  # Add the corresponding divisor
                    sumofdiv += N // num
        
        return 1 if sumofdiv == N else 0  # Return 1 if perfect, otherwise 0
