import sys
input = sys.stdin.readline

result = []
for _ in range(int(input())):
    n = int(input())
    if n == 0 and result:
        result.pop()
    else:
        result.append(n)

print(sum(result))