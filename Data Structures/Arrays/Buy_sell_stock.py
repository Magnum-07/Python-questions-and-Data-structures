A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
# print(A.sort(reverse=True))


def buy_sell_stock(arr):
    diff = 0
    min_el = arr[0]

    for i in range(1,len(arr)):
        min_el = min(arr[i], min_el)

        if arr[i] - min_el > diff:
            diff = arr[i] - min_el
    return diff


print(buy_sell_stock(A))