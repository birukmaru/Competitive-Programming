class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum={}
        prefix_sum[-1]=0
        for i in range(len(nums)):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
        min_val=min(i for i in prefix_sum.values())
        return abs(min_val)+1
        