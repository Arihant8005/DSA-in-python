arr = [5, 9, 4, 3, 1]
target = 9
result = []
def backtrack(index, total, subset):
    if(total == target):
        result.append(subset.copy())
        return
    elif(total > target):
        return
    if(index >= len(arr)):
        return
    subset.append(arr[index])
    sum = total + arr[index]
    backtrack(index+1, sum, subset)
    e = subset.pop()
    sum -= e
    backtrack(index+1, sum, subset)

backtrack(0, 0, [])
print(len(result))