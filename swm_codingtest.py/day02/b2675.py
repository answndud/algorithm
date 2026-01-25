import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, s = input().split()
    n = int(n)
    s = str(s).rstrip()
    result = []
    for i in s:
        result.append(int(n) * i)
    print(''.join(result))