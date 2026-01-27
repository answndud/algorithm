# # queue
# from collections import deque

# def solution(prices):
#     queue = deque(prices)
#     answer = []
    
#     while queue:
#         price = queue.popleft()
#         sec = 0
#         for q in queue:
#             sec += 1
#             if price > q:
#                 break
#         answer.append(sec)
#     return answer

'''
1. 각 시점 i에 대해 **“처음으로 가격이 떨어지는 시점”**을 찾는 문제다.
2. i마다 뒤를 보면 O(N²) → 아직 안 떨어진 인덱스만 스택에 보관한다.
3. 새 가격이 들어올 때, 스택 top 가격보다 작으면 그 인덱스는 지금 떨어진 것 → pop하며 시간 계산.
4. while을 써도 각 인덱스는 push 1번, pop 1번이라 전체는 O(N).
5. 끝까지 남은 인덱스들은 마지막까지 버틴 시간(n − 1 − i) 로 처리한다.

관찰: 가격이 계속 오르거나 유지되면, 가격이 언제 떨어질지 알 수 없음. 일단 스택에 넣고 기다림
사건: 현재 가격이 스택(대기중)에 있는 가격보다 낮아지면 스택을 꺼냄
계산: 현재시간 - 대기실에 들어갔던 시간이 유지된 기간이 됨
'''

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = [] # 값이 아니라 가격이 아직 떨어지지 않은 인덱스를 담음
    
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top # 떨어진 시점 - 들어온 시점
        stack.append(i) # 현재 시간을 stack에 추가
    
    while stack: # 끝까지 가격이 안떨어진 경우
        top = stack.pop()
        answer[top] = n - 1 - top # 전체 시간 - 들어온 시점
    return answer