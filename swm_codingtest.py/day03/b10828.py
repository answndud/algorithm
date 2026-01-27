import sys
input = sys.stdin.readline

stack = []
for i in range(int(input())):
    s = input().rstrip()
    if s.startswith("push"):
        array = s.split()
        stack.append(int(array[1]))
    elif s == "top":
        print(stack[-1]) if stack else print(-1)
    elif s == "empty":
        print(0) if stack else print(1)
    elif s == "size":
        print(len(stack)) if stack else print(0)
    elif s == "pop":
        print(stack.pop()) if stack else print(-1)