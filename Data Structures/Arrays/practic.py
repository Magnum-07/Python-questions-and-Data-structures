def hourglassSum(arr):
    # start = 0
    # end = 3
    i = 0
    j = 1
    k = 2
    new_ls = list()
    for a in range(4):
        for b in range(4):
            start = b
            end = b + 3
            sum_el = 0
            for a in range(start, end):
                val_1 = arr[i][a]
                val_2 = arr[j][start + 1]
                val_3 = arr[k][a]
                sum_el += val_1 + val_3
            new_ls.append(sum_el + val_2)
        i += 1
        j += 1
        k += 1

    return max(new_ls)
