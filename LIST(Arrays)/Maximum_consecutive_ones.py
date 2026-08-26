# Given a binary array nums, return the maximum number of consecutive 1's in the array.

nums = [1,1,0,1,1,1]

count = 0
max_count = 0
for val in nums:
    if(val == 1):
        count += 1
    else:
        max_count = max(count, max_count)
        count = 0
print(max(count,max_count))