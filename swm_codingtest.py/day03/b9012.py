import sys
input = sys.stdin.readline


for _ in range(int(input())):
    stack = []
    array = input().rstrip()
    for i in array:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        print("YES") if not stack else print("NO")