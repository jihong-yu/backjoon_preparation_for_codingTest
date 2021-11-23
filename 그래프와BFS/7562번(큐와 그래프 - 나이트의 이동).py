import sys
from collections import deque

input = sys.stdin.readline


def bfs(startx, starty, desx, desy):  # 시작점 x,y, 목적지 x,y
    queue = deque()
    queue.append([startx, starty])  # 우선 시작점x,y를 큐에 넣는다.

    while queue:
        x, y = queue.popleft()  # 큐에 있는 x,y를 뺀다.

        if x == desx and y == desy:  # 만약 그 x,y가 목적지 x,y라면
            return graph[x][y]  # 목적지(x,y)에 저장되어 있는 값을 리턴한다.

        for i in range(8):  # 각 이동할 수 있는 좌표를 돈다.
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= I or ny >= I or nx < 0 or ny < 0:  # 만약 좌표가 그래프범위를 벗어나면 continue
                continue

            if graph[nx][ny] == 0:  # 만약 점(nx,ny)를 아직 방문하지 않았다면
                queue.append([nx, ny])  # 그 점을 append하고
                graph[nx][ny] = graph[x][y] + 1  # 그 점의 값을(이동횟수의 최소값) 전의 값에서 + 1 해준다.


T = int(input())
for _ in range(T):
    I = int(input())  # 그래프의 크기 입력
    startx, starty = map(int, input().split())  # 시작점 입력
    desx, desy = map(int, input().split())  # 목적지 입력
    graph = [[0] * I for _ in range(I)]  # 그래프를 I크기 만큼 0으로 초기화

    dx = [-2, -1, 1, 2, -2, -1, 1, 2]  # 행이동좌표
    dy = [1, 2, 2, 1, -1, -2, -2, -1]  # 열이동좌표

    print(bfs(startx, starty, desx, desy))
