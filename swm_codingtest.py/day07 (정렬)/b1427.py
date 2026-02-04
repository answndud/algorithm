import sys
input = sys.stdin.readline

n = input().rstrip()
array = []
for i in n:
    array.append(int(i))
array.sort(reverse=True)
print(''.join(map(str, array)))