import sys, bisect
input = sys.stdin.readline


n = int(input())
nums = sorted(list(map(int, input().split())))
m = int(input())
target_list = list(map(int, input().split()))

def search(start, end, target):
    if start == end:
        if nums[start] == target:
            print(1)
        else:
            print(0)
        return
    mid = (start + end) // 2
    if nums[mid] < target:
        search(mid + 1, end, target)
    else:
        search(start, mid, target)

for i in target_list:
    search(0, n - 1, i)
    
    
# for i in target_list:
#     index = bisect.bisect_left(nums, i)
#     if index < len(nums) and nums[index] == i:
#         print(1)
#     else:
#         print(0)