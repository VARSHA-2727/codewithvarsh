class Solution:
	def twoSum(self, arr, target):
	    n =len(arr)
	    seen=set()
	    for n in arr:
	        c=target-n
	        if c in seen:
	            return True
	        seen.add(n)
	    return False
	    
