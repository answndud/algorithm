import sys
input = sys.stdin.readline

h, m = map(int, input().split())

if m >= 45:
    print(f"{h} {m - 45}")
else:
    x_m = 60 - abs(m - 45)
    if h == 0:
        x_h = 23
    else:
        x_h = h - 1
    print(f"{x_h} {x_m}")