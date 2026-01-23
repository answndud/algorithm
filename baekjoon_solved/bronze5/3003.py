arr = [1, 1, 2, 2, 2, 8]
input_arr = list(map(int, input().split()))
result = []

for i in range(6):
    if arr[i] == input_arr[i]:
        result.append(0)
    else:
        result.append(arr[i] - input_arr[i])

print(*result)