class Solution:
    def reverse_exponentiation(self, n):
        # Reverse the digits of n by converting to string, reversing, and converting back to integer
        reversed_n = int(str(n)[::-1])
        # Compute n raised to the power of reversed_n
        return n ** reversed_n
