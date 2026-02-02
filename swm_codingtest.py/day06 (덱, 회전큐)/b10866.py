import sys
from collections import deque
input = sys.stdin.readline

d = deque()
for _ in range(int(input())):
    arr = list(map(str, input().split()))
    if arr[0] == "push_front":
        d.appendleft(int(arr[1]))
    elif arr[0] == "push_back":
        d.append(int(arr[1]))
    elif arr[0] == "pop_front":
        print(d.popleft()) if d else print(-1)
    elif arr[0] == "pop_back":
        print(d.pop()) if d else print(-1)
    elif arr[0] == "size":
        print(len(d))
    elif arr[0] == "empty":
        print(0) if d else print(1)
    elif arr[0] == "front":
        print(d[0]) if d else print(-1)
    elif arr[0] == "back":
        print(d[-1]) if d else print(-1)
            
    