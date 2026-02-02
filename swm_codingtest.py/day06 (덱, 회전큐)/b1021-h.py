from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
targets = list(map(int, input().split()))

dq = deque(range(1, n + 1))
answer = 0

for t in targets:
    index = dq.index(t)
    
    left_cost = index
    right_cost = len(dq) - index
    
    if left_cost <= right_cost:
        answer += left_cost
        for _ in range(left_cost):
            dq.append(dq.popleft())
    else:
        answer += right_cost
        for _ in range(right_cost):
            dq.appendleft(dq.pop())
    dq.popleft()
print(answer)


'''
strategy: deque, greedy
1. 현재 큐에서 타켓 넘버의 인덱스 위치 찾기
2. 왼쪽 회전과 오른쪽 회전의 비용 비교
3. 비용 작은 쪽으로 돌려서 pop
'''