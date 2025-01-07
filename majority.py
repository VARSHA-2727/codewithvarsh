class Solution:
    def majority_element(nums):
    count = 0
    candidate = None

    # First pass: Find the potential candidate
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Second pass: Verify that the candidate appears more than n // 2 times
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None  # Return None if no majority element is found

# Example usage:
nums = [1, 2, 3, 4]
print(majority_element(nums))  # Output: None
