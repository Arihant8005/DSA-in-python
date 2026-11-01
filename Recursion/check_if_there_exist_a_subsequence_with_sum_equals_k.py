# Return True or False if there exists a subsequence with sum = k

arr = [5, 9, 4]
target = 9

def solve(nums, i, total, k):
    if(total == k):
        return True
    elif(total > k):
        return False
    if(i >= len(nums)):
        return False

    final_sum = total + nums[i]
    pick = solve(nums, i+1, final_sum, k)
    if(pick == True):
        return True
    final_sum = total
    Not_pick = solve(nums, i+1, final_sum, k)
    return Not_pick


print(solve(arr, 0, 0, target))


#IF we have to return atleast one subsequence
# arr = [5, 9, 4]
# target = 9
# result = []

# def solve(nums, i, total, subset, k):
#     if(total == k):
#         result.append(subset.copy())
#         return True
#     elif(total > k):
#         return False
#     if(i >= len(nums)):
#         return False
    
#     subset.append(nums[i])
#     final_sum = total + nums[i]
#     pick = solve(nums, i+1, final_sum, subset, k)
#     if(pick == True):
#         return True
#     subset.pop()
#     final_sum = total
#     Not_pick = solve(nums, i+1, final_sum, subset, k)
#     return Not_pick


# solve(arr, 0, 0, [], target)
# print(result)

