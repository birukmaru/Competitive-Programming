def pivot_index(nums):
    total=sum(nums)
    prefix_sum={}
    prefix_sum[-1]=0
    for i in range(len(nums)):
        prefix_sum[i]=nums[i]+prefix_sum[i-1]
    print(prefix_sum)
    for i in range(len(nums)):
        if prefix_sum[i-1]==total-prefix_sum[i]:
            return i
    return -1
pivot_index([1,7,3,6,5,6])