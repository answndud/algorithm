total = int(input())
x = 0
for i in range(int(input())):
    price, many = map(int, input().split())
    x += (price * many)
if total == x:
    print("Yes")
else:
    print("No")