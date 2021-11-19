import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i)


for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
