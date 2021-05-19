def arbitary_precision(arr):
    carry = 0
    # for i in range(1, len(arr)+1):
    #     size = len(arr) - i
    #     # print("Value of size is :", size)
    #     rightmost_el = arr[size]
    #     # print("Value of rightmost el is :", rightmost_el)
    #     if i == 1:
    #         # print("This got executed")
    #         add = rightmost_el + 1 + carry
    #         # print("Value of first addition of add is:", add)
    #     else:
    #         add = rightmost_el + carry
    #         # print("else also got executed, value of add rn: ", add)
    #     if add >= 10:
    #         carry = 1
    #         arr[size] = 0
    #         print(arr)
    #     else:
    #         carry = 0
    #         arr[size] = add
    #         break
    # if carry == 1:
    #     arr[0] += 10
    # return arr
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i-1] += 1
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)
    return arr


a1 = [9, 9, 9, 9]
print(arbitary_precision(a1))
