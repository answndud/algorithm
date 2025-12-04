total_seconds = 0
for _ in range(4):
    time = int(input())
    total_seconds += time
print(total_seconds // 60)
print(total_seconds % 60)