A = [-2, 1, 2, 4, 7, 11]
target = 20


# Method 1
#  time complexity is O(n^2)
#  Space complexity is O(1)
# def two_sum(arr, target_sum):
#     for i in range(len(arr)):
#         el = arr[i]
#         for j in range(i+1, len(arr)):
#             if el + arr[j] == target_sum:
#                 return True
#
#     return False

# Method2
#  time complexity is O(n)
#  Space complexity is O(n)
# def two_sum(arr, target_sum):
#     ht = dict()
#     for i in range(len(arr)):
#         if arr[i] in ht:
#             print(arr[i], ht[arr[i]])
#             return True
#         else:
#             ht[target_sum - arr[i]] = arr[i]
#     return False

# Method 3
#  time complexity is O(n)
#  Space complexity is O(1)
def two_sum(arr, target_sum):
    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] + arr[j] == target_sum:
            print(arr[i], arr[j])
            return True
        elif arr[i] + arr[j] > target_sum:
            j -= 1
        else:
            i += 1
    return False


print(two_sum(arr=A, target_sum=13))
