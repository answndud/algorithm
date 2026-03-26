def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    best = 0

    def dfs(cur_k, cnt):
        nonlocal best
        if cnt > best:
            best = cnt

        for i in range(n):
            if visited[i]:
                continue
            need, cost = dungeons[i]
            if cur_k >= need:
                visited[i] = True
                dfs(cur_k - cost, cnt + 1)
                visited[i] = False

    dfs(k, 0)
    return best

'''
전형적인 완전탐색(백트래킹, dfs)문제
1.	“순서가 결과를 바꾼다” → 순열/백트래킹
2.	n<=8 → 완전탐색 OK
3.	DFS로 “갈 수 있으면 들어가고, 방문 표시하고, 되돌리기”
'''