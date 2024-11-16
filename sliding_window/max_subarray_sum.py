def max_subarray_sum(arr,k):
    window_sum=sum(arr[:k])
    max_sum=window_sum
    for end in range(k,len(arr)):
        window_sum=window_sum + arr[end]
        window_sum=window_sum - arr[end-k]
        max_sum=max(max_sum,window_sum)
    return max_sum