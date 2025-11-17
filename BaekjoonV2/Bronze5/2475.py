li = list(map(int, input().split()))
li2 = [i**2 for i in li]
print(sum(li2) % 10)