'''
N * M 크기의 얼음 틀이 있음. 구멍이 뚫려 있으면0, 칸막이 존재하면 1
구멍이 뚫려 있는 부분끼리 상,하,좌,우 붙어있으면 연결되어 있는 것으로 간주
얼음 틀 모양이 주어졌을 때, 생성되는 총 아이스크림 개수 구하시오

첫 번째 줄에 얼음틀의 세로 길이 N, 가로 길이 M이 주어짐
두 번째 줄부터 N + 1번째까지 얼음 틀의 형태가 주어짐

한번에 만들 수 있는 아이스크림 개수를 출력
'''

'''
DFS
1. 시작 지점부터 상하좌우 살펴본 뒤 주변 지점 값이 0이면서 아직 방문하지 않았다면 방문
2. 방문한 지점에서 다시 상하좌우 살피면서 방문 진행 -> 연결된 모든 지점 방문 가능
3. 모든 노드에 대하여 1~2번의 과정을 반복, 방문하지 않은 지점 수를 카운트 
'''
import sys
input = sys.stdin.readline()

def dfs(x, y): # 특정 노드를 방문하고 연결된 모든 노드들 방문
    # 주어진 범위 벗어나는 경우에 종료
    if x <= -1 or x >= m or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

n, m = map(int, input().split)

# 2차원 리스트의 맵 정보 입력 받기
graph = [] 
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)