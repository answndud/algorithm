import sys

input = sys.stdin.readline

for _ in range(int(input())):
    left, right = [], []
    password = input().rstrip()
    
    for i in password:
        if i == ">":
            if right:
                left.append(right.pop())
        elif i == "<":
            if left:
                right.append(left.pop())
        elif i == "-":
            if left:
                left.pop()
        else:
            left.append(i)
    left.extend(reversed(right))
    print(''.join(left))