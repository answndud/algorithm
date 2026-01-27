import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque([i for i in range(1, n + 1)])
result = []
while True:
    if len(queue) == 1:
        result.append(str(queue[0]))
        break
    for i in range(k - 1):
        queue.append(queue.popleft())
    result.append(str(queue.popleft()))
    
print('<' + ', '.join(result) + '>')