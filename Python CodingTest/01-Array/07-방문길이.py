def solution(dirs):    
    x, y = 5, 5
    answer = set()
    
    for dir in dirs:
        nx, ny = update_location(x, y, dir)
        if not is_valid_move(nx, ny):
            continue # 벗어난 좌표 인정 안함. 무시하고 다음 이동
        # a에서 b로 간 경우, b에서 a도 추가해야 함(총 경로의 개수는 방향성이 없음)
        answer.add((x, y, nx, ny))
        answer.add((nx, ny, x, y))
        x, y = nx, ny # 좌표 업데이트
    
    return len(answer) / 2

def is_valid_move(nx, ny):
    return 0 <= nx < 11 and 0 <= ny < 11

def update_location(x, y, dir):
    if dir == 'U':
        nx, ny = x, y + 1
    elif dir == 'D':
        nx, ny = x, y - 1
    elif dir == 'L':
        nx, ny = x - 1, y
    elif dir == 'R':
        nx, ny = x + 1, y
    return nx, ny

'''
중복 경로는 최종 길이에 포함되지 않는다.
그러면 이동자체를 카운팅 하는게 아니고 이동한 좌표를 담아서 set() 처리.

구현문제는 답안 코드의 길이가 긴 경우가 많으므로 기능별로 함수를 구현하는게 좋다.
'''

# 위의 문제를 훨씬 간결하게
# def solution(dirs):
#     s = set()
#     d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
#     x, y = 0, 0
#     for i in dirs:
#         nx, ny = x + d[i][0], y + d[i][1]
#         if -5 <= nx <= 5 and -5 <= ny <= 5:
#             s.add((x,y,nx,ny))
#             s.add((nx,ny,x,y))
#             x, y = nx, ny
#     return len(s)//2
