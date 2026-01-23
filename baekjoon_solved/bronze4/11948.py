array = []
for i in range(4):
    score = int(input())
    array.append(score)

e = int(input())
f = int(input())

array = sorted(array)
array.pop(0)

x = max(e, f)

print(sum(array) + x)