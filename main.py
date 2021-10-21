import sys

sys.setrecursionlimit(100001)
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))
visited = [False for _ in range(N)]
ans = int(1e9)


def dfs(depth, idx):
    global ans
    if depth == N // 2:
        start, link = 0, 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += array[i][j]
                elif not visited[i] and not visited[j]:
                    link += array[i][j]
        print(start, link)
        ans = min(ans, abs(start - link))

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False


dfs(0, 0)
print(ans)
