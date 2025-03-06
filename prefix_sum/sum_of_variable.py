class Solution:
    def subarraySum(self, nums) -> int:
        N=len(nums)
        total=0
        for i in range(N):
            start=max(0,i-nums[i])
            total=total + sum(nums[start:i+1])
        return total







        # left_sum=0
        # res=0
      
        # for i in range(1,len(nums)):
        #     start= max(0,i-nums[i])
        #     if start==0:
        #         nums[i]=nums[i]+nums[i-1]
        #     else:
        #         nums[i]=nums[i]+nums[i-1]-nums[start-1]
            
        # print(nums)
        # return sum(nums)
        