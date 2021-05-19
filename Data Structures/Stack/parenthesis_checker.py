open_p = ["[", "{", "("]
close_p = ["]", "}", ")"]


def paren_checker(check_str):
    stack = []
    for i in check_str:
        if i in open_p:
            stack.append(i)
        elif i in close_p:
            pos = close_p.index(i)
            if (len(stack) > 0) and (open_p[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "unbalanced"

    if len(stack) == 0:
        return "balanced"
    else:
        return "unbalanced"


print(paren_checker("[{}]"))
