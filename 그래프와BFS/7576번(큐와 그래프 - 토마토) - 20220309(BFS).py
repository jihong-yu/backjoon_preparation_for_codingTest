import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

graph = []  # 입력받을 그래프를 담을 리스트 선언

count_zero = 0  # 0의 개수를 셀 변수
queue = deque()  # 1의 좌표를 담을 큐 선언

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j] == 1:
            queue.append((i, j))
        elif temp[j] == 0:
            count_zero = 1
    graph.append(temp)

# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 으로 한칸 씩 이동할 좌표 설정
dr = [-1, 0, +1, 0]  # 행 상 우 하 좌
dc = [0, +1, 0, -1]  # 열 상 우 하 좌

if count_zero == 0:
    print(0)
else:
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M or graph[nr][nc] != 0:
                continue

            graph[nr][nc] = graph[r][c] + 1
            queue.append([nr, nc])

    count_zero = 0
    max_ = 0
    for i in range(N):
        count_zero = graph[i].count(0)
        if count_zero > 0:
            break
        temp_max = max(graph[i])
        if temp_max > max_:
            max_ = temp_max

    if count_zero > 0:
        print(-1)
    else:
        print(max_ - 1)
