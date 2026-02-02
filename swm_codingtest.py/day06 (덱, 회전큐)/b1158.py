from collections import deque
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
q = deque(range(1, n + 1))
result = []

while True:
    if len(q) == 1:
        result.append(q[0])
        break
    
    for _ in range(k - 1):
        q.append(q.popleft())
        
    result.append(q.popleft())
    
print('<' + ', '.join(map(str, result)) + '>')