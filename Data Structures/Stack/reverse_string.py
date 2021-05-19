input_str = "Hello"
stack = []
for i in input_str:
    stack.append(i)

while len(stack) != 0:
    # el = stack.pop()
    print(stack.pop(), end="")

# Another methods
# 1. Using slicing
# print(input_str[::-1])

# 2. Using inbuilt reversed() function
# print("".join(list(reversed(input_str))))