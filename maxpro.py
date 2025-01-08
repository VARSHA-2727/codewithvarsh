class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		max_pro=arr[0]
		min_pro=arr[0]
		result=arr[0]
		for i in range(1,len(arr)):
		    num=arr[i]
		    if num<0:
		        max_pro,min_pro=min_pro,max_pro
		    max_pro=max(num,max_pro*num)
		    min_pro=min(num,min_pro*num)
		    result=max(result,max_pro)
		return result
