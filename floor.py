class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,k):
        n=len(arr)
        floor=-1
        for i in range(n):
            if arr[i]<=k:
                floor=i
        return floor
        
