def solution(s: str):
    result = 0
    for i in s:
        if i == "(":
            result += 1
        elif i == ")":
            result -= 1
    return result is 0


def solution2(s: str):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True