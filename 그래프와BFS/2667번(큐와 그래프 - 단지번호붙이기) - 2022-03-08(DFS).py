import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = []  # 입력받을 그래프를 담을 리스트 선언

dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌

count = 0
danzi_count = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))


def dfs(r, c, cnt):
    global danzi_cnt

    danzi_cnt += 1
    graph[r][c] = 0

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or graph[nr][nc] != 1:
            continue

        dfs(nr, nc, cnt + 1)


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            danzi_cnt = 0
            dfs(i, j, 1)
            danzi_count.append(danzi_cnt)
            count += 1

print(count)
for cnt in sorted(danzi_count):
    print(cnt)
