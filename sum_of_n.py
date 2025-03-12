class Solution:
	def find(self, n):
	    t_sum=0
		for s in range(1,n+1):
		        t_sum+=s
		        if t_sum==n:
		            return s
		        elif t_sum>n:
		            return -1
        return -1
