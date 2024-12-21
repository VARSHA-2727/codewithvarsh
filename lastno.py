class Solution:
    def getLastDigit(self, a, b):
        a=int (a)%10
        b=int(b)
        if b==0:
            return 1
        return pow(a,b,10)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b=map(str,input().split())
        
        ob = Solution()
        print(ob.getLastDigit(a,b))
# } Driver Code Ends
        
