n = int(input())
line1 = 0
line3 = 0

for i in range(1, n + 1):
    line1 += i
    line3 += i**3

print(line1)
print(line1**2)
print(line3)