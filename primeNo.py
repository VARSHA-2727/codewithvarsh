class Solution:
    def isPrime(self, n):
        for i in range (1,n+1):
            if(n%i==0):
                return True
            else:
                return False


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n = int(input())  # Read the number to check primality

        ob = Solution()
        # Using Python's conditional expression for true/false
        print("true" if ob.isPrime(n) else
              "false")  # Print "true" if prime, else "false"
        print("~")

# } Driver Code Ends
