import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

array = []
# array.append(x)
# array.append(y)
# array.append(w - x)
# array.append(h - y)
array.extend([x, y, w - x, h - y])

print(min(array))