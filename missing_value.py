class Solution:
    def missingNumber(self, arr):
        n=len(arr)+1
        total=n*(n+1)//2
        actual_sum=sum(arr)
        miss=total-actual_sum
        return miss
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends
