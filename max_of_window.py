class Solution:
    def maxOfSubarrays(self, arr, k):
        n=len(arr)
        result=[]
        for i in range(n-k+1):
            max=arr[i] 
            for j in range(i,k+1):
                if arr[j]>max:
                    max=arr[j] 
            result.append(max)
        return result
