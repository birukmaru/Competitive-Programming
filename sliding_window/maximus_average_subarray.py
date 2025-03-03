def findMaxAverage(self, nums, k):
    window_sum=sum(nums[:k])
    max_sum=window_sum
    for i in range(k,len(nums)):
        window_sum=window_sum+nums[i]
        window_sum=window_sum-nums[i-k]
        max_sum=max(max_sum,window_sum)
    average=float(max_sum)/k
    return average
        