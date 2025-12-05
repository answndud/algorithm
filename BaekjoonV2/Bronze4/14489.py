w1, w2 = map(int, input().split())
c = int(input())

if (c * 2) > w1 + w2:
    print(w1 + w2)
else:
    print(w1 + w2 - (c * 2))