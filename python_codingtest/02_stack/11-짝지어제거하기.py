def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return int(not stack) # 스택이 비어있으면 1, 있으면 0 반환