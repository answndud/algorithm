from collections import deque

def solution(priorities, location):
    queue = deque([(v, i) for i, v in enumerate(priorities)])
    answer = 0
    
    while queue:
        current = queue.popleft()
        
        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else:
            answer += 1
            if current[1] == location:
                return answer
            
            
'''
1. 데이터 구조화: 각 프로세스의 중요도와 인덱스를 한 쌍으로 묶어 큐에 넣음.
2. 중요도 확인: 큐에서 프로세스 하나 꺼낸 뒤, 큐에 남아있는 프로세스들 중
더 높은 중요도가 있는지 확인
3. 조건부 처리:
    - 더 높은 중요도가 있다면 다시 큐의 맨 뒤로 보냄
    - 내가 제일 높다면 실행 횟수 카운트하고, 만약 이 프로세스가 찾던 location의 프로세스라면
    실행 횟수 반환
'''