def containsNearbyDuplicate(self, nums, k) -> bool:
    hashed={}
    for i in range(len(nums)):
        if nums[i] in hashed:
            if abs(hashed[nums[i]]-i)<=k:
                return True
            else:
                hashed[nums[i]]=i
        else:
            hashed[nums[i]]=i
    return False