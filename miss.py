class Solution:
    def missingNumber(self, nums):
        tot=nums*(nums+1)//2
        acc_sum=sum(len(nums))
        miss_num=tot-acc_sum
        return miss


        
