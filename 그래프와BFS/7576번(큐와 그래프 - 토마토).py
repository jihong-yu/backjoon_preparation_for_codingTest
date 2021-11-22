import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
queue = deque()  # 1의 위치를 담을 큐 선언
count = 0  # 그래프의 0의 개수를 셀 count값 선언
result = 0  # 결과값을 출력할 result값 선언
graph = []  # 입력받을 그래프를 담을 리스트 선언

for i in range(N):
    graph.append(list(map(int, input().split())))
    count += graph[i].count(0)  # 해당그래프를 입력받으면서 0의 개수를 같이 센다

# 만약 그래프에 0값이 없다면 모두 익었다는 말이므로 바로 0을 출력 후 종료
if count == 0:
    print(0)
    exit()

# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 으로 한칸 씩 이동할 좌표 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]  # 행값
            ny = y + dy[i]  # 열값

            # 만약 이동한 좌표가 그래프 범위 벗어나면 continue 처리
            if nx >= N or ny >= M or nx < 0 or ny < 0:
                continue

            # 만약 위치를 이동했는데 그 좌표값이 0이라면
            if graph[nx][ny] == 0:
                queue.append([nx, ny])  # 새로운 좌표값을 큐에 추가한 후
                graph[nx][ny] = graph[x][y] + 1  # 새로운 좌표값을 전의 좌표값에서 +1해준다.


# 1인 좌표 모두 큐에 넣어주기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])

bfs()

count = 0  # 0을 셀 count값을 0으로 선언
for i in graph:  # bfs를 돈 그래프를 돈다.
    count += i.count(0)  # 0의 개수를 센다.
    if count > 0:  # 만약 0이 존재한다면
        print(-1)  # -1을 출력하고
        exit()  # 바로 종료

    # 0이 존재하지 않는다면
    result = max(result, max(i))  # 결과값에 그래프의 행마다 최대값을 계속 대입해준다.

print(result - 1)  # 시작할 때부터 1로 시작하기 때문에 출력값에 -1을 해줘야 한다.
