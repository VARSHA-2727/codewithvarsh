#User function Template for python3
class Solution:
    def armstrongNumber(self, n):
        # Check if n is a three-digit number
        if 100 <= n < 1000:
            # Calculate the sum of the cubes of its digits
            sum_of_cubes = sum(int(d) ** 3 for d in str(n))
            # Return True if it is an Armstrong number, else False
            return sum_of_cubes == n
        else:
            return False 
