def dfs(depth, start):
    global exit_check

    if exit_check:
        return

    if depth == 4:
        exit_check = True
        return

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i)
            visited[i] = False


N, M = map(int, input().split())

# 친구관계 저장
graph = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * N
exit_check = False
for i in range(N):
    visited[i] = True
    dfs(0, i)
    visited[i] = False

if exit_check:
    print(1)
else:
    print(0)
