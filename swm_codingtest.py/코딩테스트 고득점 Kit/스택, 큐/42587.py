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