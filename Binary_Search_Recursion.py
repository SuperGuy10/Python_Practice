def binaryRecursion(nums,l,r,num):
    mid = (l+r)//2
    if num == nums[mid]:
        return mid
    elif num < nums[mid]:
        return binaryRecursion(nums, l, mid-1, num)
    else:
        return binaryRecursion(nums, mid+1, r, num)

nums = [1,2,3,4,5,6,7,8,9]
print(binaryRecursion(nums,0,len(nums)-1,9))
