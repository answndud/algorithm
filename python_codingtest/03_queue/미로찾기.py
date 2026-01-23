# BFS(Breadth-First Search, 너비 우선 탐색)
# Queue 사용

'''
선제조건: array의 길이(len)가 0이면 return False. 더 이상 갈 곳이 없음
1. array[0] 확인해서 그 위치로 올라가고, array[0] 삭제. 지도 위 올라간 지점 -1 표시
2. 이동 가능한 지점을 확인하여 array에 저장
중간조건: 도착 지점이 array에 있는게 확인되면 return True. 목적지에 도달 가능한거 확인
3. 1번으로 돌아감
'''

def search_and_update(now_pos, now_map, now_arr):
    h, w = len(now_map), len(now_map[0])
    now_x, now_y = now_pos
    
    # 상, 하, 좌, 우 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        
        # 수정: nx < h 로 변경 (인덱스 범위 준수)
        if 0 <= nx < h and 0 <= ny < w:
            if now_map[nx][ny] == 0:
                now_arr.append([nx, ny])
                now_map[nx][ny] = -1 # 방문 마킹
                
    # 수정: raise 대신 return 사용
    return now_arr


def can_go(start, end, map_):
    # 시작점 예외 처리
    if map_[start[0]][start[1]] == 1:
        return False

    arr = [start]
    map_[start[0]][start[1]] = -1 

    while len(arr) != 0:
        now_position = arr.pop(0)
        
        # 목적지에 도달했는지 확인
        if now_position == end: 
            return True
            
        arr = search_and_update(now_position, map_, arr)
        
    return False

map_data = [
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1]
]

result = can_go([0, 0], [5, 4], map_data)
print(f"도달 가능 여부: {result}")