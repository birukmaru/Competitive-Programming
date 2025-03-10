class Solution:
    def countPartitions(self, nums) -> int:
        total=sum(nums)
        count=0
        left_sum=0
        for i in range(len(nums)-1):
            nums[i]=nums[i] + left_sum
            left_sum=nums[i]
            if (2*nums[i]-total)%2==0:
                count += 1      
        return count


        # for i in range(1,len(nums)):
        #     nums[i]=nums[i]+nums[i-1]
        # for i in range(len(nums)-1):
        #     if (2*nums[i]-nums[-1])%2==0:
        #         count += 1
        # return count


        