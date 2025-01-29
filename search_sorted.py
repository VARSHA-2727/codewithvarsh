class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        n=len(arr)
        if n==0:
            return None
        for i in range(n):
            if arr[i]==k:
                return True
        return False
