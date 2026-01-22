import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]
    
count = 0
max_v = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def bfs(y, x):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if arr[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))
    return rs
    

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and chk[i][j] == False:
            chk[i][j] = True
            count += 1
            max_v = max(max_v, (bfs(i, j)))
            
print(count)
print(max_v)