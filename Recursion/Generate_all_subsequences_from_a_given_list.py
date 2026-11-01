nums = [9, 5, 7]
result = []
def generate(i, arr, subset):
    if(i >= len(arr)):
        result.append(subset.copy())
        return

    subset.append(arr[i])
    generate(i+1, arr, subset)
    subset.pop()
    generate(i+1, arr, subset)

generate(0, nums, [])
print(result)

# T.C = O(2^n)
# S.C = O(n)