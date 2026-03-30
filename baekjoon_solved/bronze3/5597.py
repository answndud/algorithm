import sys
input = sys.stdin.readline

students = [False] * 31

for _ in range(28):
    num = int(input())
    students[num] = True

for i in range(1, 31):
    if students[i] is False:
        print(i)