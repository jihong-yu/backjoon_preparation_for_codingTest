import sys
from collections import deque


input = sys.stdin.readline

def bfs(start_r, start_c):
    global count

    queue = deque([[start_r, start_c]])
    danzi_cnt = 1
    graph[start_r][start_c] = 0
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N or graph[nr][nc] != 1:
                continue

            graph[nr][nc] = 0
            queue.append([nr, nc])
            danzi_cnt += 1

    count += 1
    danzi_count.append(danzi_cnt)


N = int(input())

graph = []  # 입력받을 그래프를 담을 리스트 선언

dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌

count = 0
danzi_count = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j)

print(count)
for cnt in sorted(danzi_count):
    print(cnt)
