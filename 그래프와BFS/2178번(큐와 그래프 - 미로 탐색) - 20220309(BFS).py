import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(N)]  # 입력받을 그래프를 담을 리스트 선언

queue = deque([[0, 0]])

dr = [-1, 0, +1, 0]  # 행 상 우 하 좌
dc = [0, +1, 0, -1]  # 열 상 우 하 좌


while queue:

    r, c = queue.popleft()

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= M or graph[nr][nc] != 1:
            continue

        graph[nr][nc] = graph[r][c] + 1
        queue.append([nr, nc])


print(graph[N - 1][M - 1])
