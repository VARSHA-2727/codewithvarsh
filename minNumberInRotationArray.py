class Solution:
    
    #Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr,low,high):
        left, right = 0, len(arr) - 1
    
        while left < right:
            mid = (left + right) // 2
            if arr[mid]> arr[right]:
                left = mid + 1  # Minimum is in the right half
            else:
                right = mid  # Minimum is in the left half or at mid
    
        return arr[left]
        

