def find_single_instance(nums):
    unique = 0
    seen = {}
    for num in nums:
        if num in seen.keys:
            seen[num] += 1
        else:
            seen[num] = 1
        

nums = [4,1,2,1,2]