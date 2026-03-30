n = int(input())

# 위쪽 삼각형
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

# 아래쪽 삼각형
for i in range(n - 1, 0, -1):
    spaces = n - i
    stars = i * 2 - 1
    print(" " * spaces + "*" * stars)