import sys

n, x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

result = []
for i in a:
    if i < x:
        result.append(i)
        
print(*result)