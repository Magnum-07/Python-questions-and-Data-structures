# num = 1237689
# import math
#
#
# def int_to_binary(num):
#     stack = []
#     txt = ""
#     while num != 0:
#         result = num % 2
#         stack.append(math.floor(result))
#         num = num // 2
#
#     while len(stack) != 0:
#         top = stack.pop()
#         txt += str(top)
#
#     return txt
#
#
# print(int_to_binary(num))
# num = 242
# print(bin(num).replace("0b",""))

def int_to_bin(num):
    if num > 1:
        int_to_bin(num//2)

    print(num % 2, end="")

int_to_bin(123789)
print("")
print(int("11110001110001101",2))