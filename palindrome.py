class Solution:
    def isPalindrome(self, n):
		n=str(n)
		rev=int(n[::-1])
		n=int(n)
		if n==rev:
		    return True
        else:
            return False
