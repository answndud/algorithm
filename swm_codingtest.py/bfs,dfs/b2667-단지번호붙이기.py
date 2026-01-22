'''
1. idea
- 2중 for, 값 1 && 방문x => dfs
- dfs를 통해 찾은 값을 저장, 정렬, 출력

2. time complexity
- dfs: o(v + e)
- v, e: n^2, 4n^2
- v + e = 5n^2 ~= n^2 ~= 625

3. data structure
- graph store: int[][]
- visited: bool[][]
- result: int[]
'''


import sys
input = sys.stdin.readline

N = int(input())
map_ = [list(map(int, input().strip())) for _ in range(N)]
check = [[False] * N for _ in range(N)]
result = []
each = 0


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
# 2차원 리스트(maze)는 maze[행][열] 순서로 접근하므로, 인덱스 순서와 맞추기 위해 dfs(y, x)를 사용합니다.
# 즉, y는 리스트의 몇 번째 줄(row)인지, x는 그 줄에서 몇 번째 칸(column)인지를 직관적으로 나타냅니다.
def dfs(y, x): # 
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= nx < N and 0 <= ny < N:
            if map_[ny][nx] == 1 and check[ny][nx] == False:
                check[ny][nx] = True
                dfs(ny, nx)

for i in range(N):
    for j in range(N):
        if map_[i][j] == 1 and check[i][j] == False:
            # 방문 체크 표시, DFS로 크기 구하고, 크기는 결과 리스트에 추가
            check[i][j] = True
            each = 0
            dfs(i, j)
            result.append(each)
            
            
result.sort()
print(len(result))
for i in result:
    print(i)