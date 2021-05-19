A = [3, 5, 2, -4, 8, 11]
target_sum = 7


def two_sum(arr, target_value):
    seen = dict()

    for i, n in enumerate(arr):
        if n in seen:
            return [seen[n], i]
        seen[target_value - arr[i]] = i


print(two_sum(A, target_sum))
