class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        n=len(arr)
        count=0
        for i in range(n):
            for j in range(i+1,n):
                if arr[i]>arr[j]:
                    count+=1
        return count

