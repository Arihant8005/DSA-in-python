# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# T.C = O(n)
# S.C = O(n)

nums = [2,7,11,15]
target = 9

freq = {}
for i in range(len(nums)):
    remaining = target - nums[i]
    if remaining in freq:
        print([freq[remaining],i])
    else:
        freq[nums[i]] = i