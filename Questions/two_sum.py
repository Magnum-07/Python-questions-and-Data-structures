A = [3, 5, 2, -4, 8, 11]
target_sum = 7

# Time Complexity(T.C.) = O(n)
# Space Complexity(S.C.) = O(n)
def two_sum(arr, target_value):
#     To solve this question by using of hashing
    seen = dict()
    
    for i, n in enumerate(arr):
        if n in seen:
            return [seen[n], i]
        seen[target_value - arr[i]] = i


print(two_sum(A, target_sum))
