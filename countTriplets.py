class Solution:
	def countTriplet(self, arr):
	    n=len(arr)
	    arr.sort()
		count=0
		for i in range (n-1,1,-1):
		    left=0
		    right=i-1
		    while left<right:
		        if arr[left]+arr[right]==arr[i]:
		           count+=1
		           left+=1
		           right-=1
		        elif arr[left]+arr[right]<arr[i]:
		            left+=1
		        else:
		            right-=1
        return count

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countTriplet(arr)
        print(res)
        print("~")
        t -= 1
