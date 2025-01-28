class Solution:    
    #Complete this function
    def printNos(self,n):
        if n == 0:
            return
    # Recursively call the function for n-1
        self.printNos(n-1)
    # Print the current number followed by a space
        print(n,end=" ")

