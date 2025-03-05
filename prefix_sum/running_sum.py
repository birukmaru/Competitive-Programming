class Solution:
    def runningSum(self, nums):
        left_sum=0
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
        return nums

        