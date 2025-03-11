class Solution:
    def rearrangeArray(self, arr):
        result = []
        left, right = 0, len(arr) - 1  # Two pointers
        
        while left <= right:
            if left != right:
                result.append(arr[left])  # Pick from the left
                result.append(arr[right]) # Pick from the right
            else:
                result.append(arr[left])  # If odd-length, add middle element
            left += 1
            right -= 1
        
        return result
