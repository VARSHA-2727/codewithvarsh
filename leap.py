class Solution:
    def checkYear (self, n):
        if n % 4 == 0:
      
        # If it's divisible by 100, it should also be 
        # divisible by 400 to be a leap year
            if n % 100 == 0:
                return n % 400 == 0
            return True
        return False
