import sys

n = int(sys.stdin.readline())
for _ in range(n):
    s = list(sys.stdin.readline())
    result = 0
    counter = 0
    for i in s:
        if i == "O":
            counter += 1
            result += counter
        else:
            counter = 0
    print(result)