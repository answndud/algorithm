time, drink = map(int, input().split())
if 12 <= time <= 16 and drink == 0:
    print(320)
else:
    print(280)