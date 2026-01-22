def dfs_recursive(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs_recursive(graph, i, visited)
            
def dfs_stack(graph, start, visited):
    stack = [start]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            
            for i in reversed(graph[v]):
                if not visited[i]:
                    stack.append(i)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)

dfs_recursive(graph, 1, visited)
dfs_stack(graph, 1, visited)