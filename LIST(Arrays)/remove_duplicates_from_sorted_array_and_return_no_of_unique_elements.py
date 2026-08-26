nums = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))

if(len(nums) == 0):
    print(0)
i = 0
for j in range(1, len(nums)):
    if nums[i] != nums[j]:
        i += 1
        nums[i] = nums[j]

print("Number of unique elements:", i + 1)
print("Unique elements:", nums[:i + 1])