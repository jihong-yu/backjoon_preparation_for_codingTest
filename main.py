import sys

sys.setrecursionlimit(10000)


def dfs(v):
    visited[v] = True
    for e in graph[v]:
        if not visited[e]:
            dfs(e)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)

for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)
