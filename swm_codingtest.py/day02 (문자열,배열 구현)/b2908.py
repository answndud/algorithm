import sys
input = sys.stdin.readline

a, b = map(str, input().split())

new_a = []
new_a.append(a[2])
new_a.append(a[1])
new_a.append(a[0])
new_a = ''.join(new_a)

new_b = []
new_b.append(b[2])
new_b.append(b[1])
new_b.append(b[0])
new_b = ''.join(new_b)

print(max(int(new_a), int(new_b)))

# a, b = input().split()
# print(max(int(a[::-1]),int(b[::-1])))