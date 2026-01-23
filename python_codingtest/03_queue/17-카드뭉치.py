from collections import deque

def solution(cards1, cards2, goal):
    
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    while goal:
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
            goal.popleft()
        else:
            break
    if len(goal) == 0:
        return "Yes"
    else:
        return "No"
    
'''
cardsI과 card2의 길이는 N이고, goal의 길이는 M입니다. 
이를 각각 deque로 변환하기 위한 시간 복잡도는 O(N + M)이고, 
반복문에서 goal의 각 원소를 순회하는 시간 복잡도는 O(M)입니 다. 
따라서 최종 시간 복잡도는 O(N + M)입니다.
'''