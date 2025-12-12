_ = input()
arr = list(map(int, input().split()))
find = int(input())
result = 0

for i in arr:
    if i == find:
        result += 1
print(result)

# # 등장 횟수 계산
# print(arr.count(target))