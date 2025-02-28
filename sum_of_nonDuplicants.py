class Solution:
	
	def findSum(self,arr):
	    sum=arr[0]
		for i in range (1,len(arr)):
		    if arr[i]!=arr[i-1]:
		        sum+=arr[i]
	    return sum
		        
