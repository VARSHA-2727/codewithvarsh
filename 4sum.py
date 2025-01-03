# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Solution:
    def fourSum(self, nums, target):
        # Initialize result list to store quadruplets
        result = []
        
        # Sort the array to handle duplicates easily
        nums.sort()
        
        # Iterate through the array with four pointers
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                for k in range(j + 1, len(nums) - 1):
                    for l in range(k + 1, len(nums)):
                        # Check if the sum of four numbers equals the target
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            # Store the quadruplet
                            quadruplet = [nums[i], nums[j], nums[k], nums[l]]
                            
                            # Avoid duplicates by checking if the quadruplet is already in the result
                            if quadruplet not in result:
                                result.append(quadruplet)
        
        return result

# Create an instance of the Solution class
solution = Solution()

# Now call the fourSum method using the instance
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(solution.fourSum(nums, target))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
