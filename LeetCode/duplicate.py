def check_duplicates(nums):
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

nums = [1, 2, 3, 4, 5, 6, 7]
print(check_duplicates(nums))