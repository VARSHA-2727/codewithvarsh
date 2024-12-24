import math
class Solution:
    def isPerfectNumber(self, n):
        if(n<2):
            return False
        return sum(i for i in range(1,n) if n%i==0)==n


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        ans = (ob.isPerfectNumber(N))
        if (ans):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
