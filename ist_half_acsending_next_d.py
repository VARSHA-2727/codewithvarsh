#User function Template for python3
class Solution:
    def customSort(self, arr):
        arr.sort()  # Step 1: Sort the array (O(N log N))
        n = len(arr)
        res = []
        left, right = 0, n - 1
        
        while left <= right:
            res.append(arr[left])  # Pick smallest element
            left += 1
            
            if left <= right:  # Avoid duplicate middle element in odd-length arrays
                res.append(arr[right])  # Pick largest element
                right -= 1
        
        return res
