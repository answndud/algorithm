import sys
input = sys.stdin.readline

n = int(input())
x = 1
for i in range(1, n + 1):
    x = x * i
print(x)

# 재귀
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(n))