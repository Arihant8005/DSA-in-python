# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements

# T.C. = O(n)
# S.C = O(1)

nums = [0,1,0,3,12]

n = len(nums)
i = 0
for j in range(n):
    if(nums[j] != 0):
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
print(nums)