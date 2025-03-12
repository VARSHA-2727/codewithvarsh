class Solution:
    def isPalindrome(self, s: str) -> bool:
		n=str(s)
		rev=(s[::-1])
		if rev==n:
		    return True
	    return False
