import sys
from collections import deque


def bfs(start, group):
    global error

    queue.append(start)
    visited[start] = group
    while queue:

        node = queue.popleft()

        for i in graph[node]:
            if not visited[i]:
                visited[i] = -visited[node]
                queue.append(i)
            elif visited[i] == visited[node]:
                error = True
                return


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    error = False
    queue = deque()
    for i in range(1, V + 1):
        if not visited[i]:
            bfs(i, 1)
            if error:
                break

    if error:
        print('NO')
    else:
        print('YES')
