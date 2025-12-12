n1 = input()
n2 = input()

n3 = int(n2[2]) * int(n1)
n4 = (int(n2[1]) * 10) * int(n1)
n5 = (int(n2[0]) * 100) * int(n1)

print(n3)
print(n4 // 10)
print(n5 // 100)
print(n3 + n4 + n5)