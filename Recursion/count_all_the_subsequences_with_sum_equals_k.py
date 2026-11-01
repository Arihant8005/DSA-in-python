arr = [5, 9, 4, 10]
target = 9

def solve(nums, i, total, k):
    if(total == k):
        return 1
    elif(total > k):
        return 0
    if(i >= len(nums)):
        return 0

    final_sum = total + nums[i]
    pick = solve(nums, i+1, final_sum, k)
    final_sum = total
    Not_pick = solve(nums, i+1, final_sum, k)
    return pick + Not_pick


print(solve(arr, 0, 0, target))