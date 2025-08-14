def minList(nums):
    min_num = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < min_num:
            min_num = nums[i]
    return min_num

# Driver Code
nums = [3, 56, 45, -6, 243, -765, 2200]
smallest = minList(nums)
print(smallest)