def findMaxRecursion(nums):
    if len(nums) == 2:
        return nums[0] if nums[0]>nums[1] else nums[1]
    subMax = findMaxRecursion(nums[1:])
    return nums[0] if nums[0] > subMax else subMax

print(findMaxRecursion([1,2,3,4,5,6,7,8]))
