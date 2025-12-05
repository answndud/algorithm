x = input()
result = 0
for i in x:
    if int(i) == 0:
        continue
    result += int(i)
print(result)