a, b, c = map(int, input().split())
x = int(a // b * c)
y = int(a * b // c)
print(max(x, y))