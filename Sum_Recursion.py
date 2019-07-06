def sumRecursion(nums):
    if nums == []:
        return 0
    return nums[0] + sumRecursion(nums[1:])
    
print(sumRecursion([3,2,5,6,7,8,9]))
