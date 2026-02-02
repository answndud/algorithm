from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    
    priorities = []
    while len(priorities) < n:
        priorities.extend(map(int, input().split()))
    
    dq = deque([(i, p)] for i, p in enumerate(priorities))
    count = 0
    
    while dq:
        idx, prio = dq.popleft()
        for _, p in dq:
            if any(p > prio):
                dq.append((idx, prio))
            else:
                count += 1
                if idx == m:
                    print(count)
                    break
    
    
    
    
    
    
'''
매 반복마다
1. 현재 큐의 앞 문서를 꺼냄
2. 나머지 큐의 문서들 중 하나라도 중요도가 더 높은 문서가 있으면
    -> 현재 문서를 맨 뒤로 다시 넣음
3. 없으면 현재 문서 출력
    - 출력 횟수 count 증가
    - 이 문서가 찾던 문서라면 -> 출력 순서 count 반환
    
중요도 비교 빠르게 하려면 any() 함수 사용
any(뒤에 있는 문서 중요도 > 현재 중요도)


'''