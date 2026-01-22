'''
N * M 크기의 직사각형 형태 미로에 갇힘. 미로에 있는 괴물을 피해 탈출해야 함
현재 위치는 (1, 1) 미로의 출구는 (N, M). 한 번에 한 칸씩 이동 가능
괴물이 있는 부분은 0. 없는 부분은 1. 미로는 반드시 탈출 할 수 있는 형태로 제공.
탈출하기 위해 움직여야 하는 최소 칸의 개수 구하여라.
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산.
'''

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))
