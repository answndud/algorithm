import sys
input = sys.stdin.readline

arr = []
for i in range(int(input())):
    num = int(input())
    arr.append(num)

for a in sorted(arr):
    print(a)