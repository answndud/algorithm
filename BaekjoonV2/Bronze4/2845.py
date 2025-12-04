l, p = map(int, input().split())
total = l * p
array = list(map(int, input().split()))
array = [i - total for i in array]
print(*array)


# L, P = map(int, input().split())
# news = list(map(int, input().split()))
# for i in news:
#     print(i - L * P, end = ' ')