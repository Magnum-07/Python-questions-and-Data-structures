# Array Advance Game

A = [3, 9, 1, 0, 2, 0, 1]
B = [3, 2, 0, 0, 2, 0, 1]
C = [1, 3, 6, 1, 0, 9]


def array_game(arr):
    furthest_value = 0
    last_idx = len(arr) - 1
    i = 0
    while i <= furthest_value < last_idx:
        furthest_value = max(furthest_value, arr[i] + i)
        i += 1
    print("Jumps required: ", i)
    return furthest_value >= last_idx
    # for k in range(len(arr)):
    #     if k <= furthest_value:
    #         furthest_value = max(furthest_value, arr[k] + k)
    #     else:
    #         return False
    #     if furthest_value > last_idx:
    #         break
    # print("Number of jumps: ", k+1)
    # return True


print(array_game(A))
print(array_game(B))
print(array_game(C))