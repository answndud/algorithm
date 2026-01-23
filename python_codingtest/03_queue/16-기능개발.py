from collections import deque

# def solution(progresses, speeds):
#     # 1. 각 작업이 완료되기까지 걸리는 '일수'를 계산하여 큐에 담습니다.
#     # math 라이브러리 없이 올림 계산: (남은진도 + 속도 - 1) // 속도
#     days_q = deque()
#     for p, s in zip(progresses, speeds):
#         remaining = 100 - p
#         day = (remaining + s - 1) // s
#         days_q.append(day)
    
#     answer = []
    
#     # 2. 큐가 빌 때까지 배포 그룹을 묶습니다.
#     while days_q:
#         # 현재 가장 앞에 있는 작업의 완료일이 기준이 됩니다.
#         first = days_q.popleft()
#         count = 1
        
#         # 3. 기준 작업보다 빨리 끝나는 뒤의 작업들을 한꺼번에 꺼냅니다.
#         while days_q and days_q[0] <= first:
#             days_q.popleft()
#             count += 1
            
#         answer.append(count)
        
#     return answer

'''
선행 작업이 완료되지 않았을 때 먼저 완료된 작업을 따로 보관하는 것은 효율성도 별로고 구현도 까다롭다.
1 각 작업의 배포 가능일을 구합니다. 
2 작업을 진행하며 배포 가능일이 첫 번째 작업일보다 빠른 작업들은 함께 배포합니다. 
3 첫 번째 작업의 배포 가능일보다 늦은 작업이 나오면, 2단계와 유사하게 해당 작업의 배포일 을 기준으로 뒤의 작업들을 배포합니다. 이를 모든 작업이 완료될 때까지 반복합니다.

'''
import math

def solution2(progresses, speeds):
    answer = []  # 각 배포마다 몇 개의 기능이 배포되는지 저장할 리스트
    n = len(progresses)  # 전체 작업(기능)의 개수
    
    # 각 작업이 완료되기까지 남은 일수를 계산하여 리스트 생성
    # (100 - 현재진도) / 속도 를 계산한 뒤, 소수점이 생기면 올림(math.ceil) 처리
    days_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)] 
    
    count = 0  # 현재 배포 그룹에 포함된 기능의 개수
    max_day = days_left[0]  # 현재 그룹의 '기준일'(가장 앞에 있는 기능의 완료일)
    
    for i in range(n):
        # 현재 작업의 완료일이 기준일(max_day)보다 작거나 같다면?
        # 즉, 앞의 기능이 끝날 때 이미 완료되어 있는 상태라면
        if days_left[i] <= max_day:
            count += 1  # 같은 그룹으로 묶어서 배포 개수 증가
        
        # 현재 작업이 기준일보다 더 오래 걸린다면 (새로운 배포 그룹 시작)
        else:
            answer.append(count)  # 지금까지 쌓인(완료된) 기능들의 개수를 결과에 추가
            count = 1  # 새 그룹의 시작: 현재 작업(새 팀장)을 카운트에 1로 포함
            max_day = days_left[i]  # 새로운 그룹의 기준일을 현재 작업의 완료일로 갱신
            
    # for문이 끝나고 마지막 그룹에 남아있는 기능 개수까지 추가
    # (더 이상 나보다 늦게 끝나는 작업이 없어서 else문에 못 들어갔던 마지막 묶음 처리)
    answer.append(count) 
    
    return answer  # 최종 배포 기록 반환