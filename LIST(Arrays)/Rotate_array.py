# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

#Method 1:
nums = [3,4,5,6,7,8,9]

k = 3
n = len(nums)
rotation = k % n
for _ in range(rotation):
    e = nums.pop()
    nums.insert(0,e)

print(nums)

#Method 2:
def reverse(nums, left, right):
    while(left < right):
        nums[left],nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

if __name__ == "__main__":
    nums = [38, 27, 43, 3, 9, 82, 10, 55]
    n = len(nums)
    k = 5
    reverse(nums, n-k, n-1)
    reverse(nums , 0, n-k-1)
    reverse(nums, 0, n-1)
    print(nums)
