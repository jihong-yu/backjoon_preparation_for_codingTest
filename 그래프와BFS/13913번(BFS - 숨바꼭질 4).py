import sys
from collections import deque

input = sys.stdin.readline


def bfs(startx, destx):  # 시작점 , 목적지 좌표
    queue = deque()
    queue.append(startx)  # 큐에 시작점 추가

    while queue:
        x = queue.popleft()  # 맨 왼쪽(들어간순서대로) 좌표 하나를 뺀다.

        if x == destx:  # 만약 그 좌표가 목적지 좌표라면
            while x != startx:  # x가 시작점이 아닐때까지 반복
                path.append(x)  # x의 값을 방문기록에 넣는다.
                x = visited[x]  # x값을 전에 방문했던 위치로 바꿔준다.
            path.append(startx)  # 마지막에 시작지점을 넣어준다.
            return graph[destx]  # 목적지 좌표에 저장되어 있는 값을 리턴

        for i in range(3):  # 좌표를 이동할 반복문
            if i != 2:  # 만약 i가 2가 아니라면
                nx = x + dx[i]  # -1,+1
            else:  # 만약 i가 2라면
                nx = x * dx[i]  # *2

            if nx < 0 or nx >= len(graph):  # 만약 그래프가 좌표를 벗어난다면
                continue  # 밑의 함수 실행x

            if graph[nx] == 0:  # 만약 그래프값이 0이면(즉, 아직 방문하지 않았다면)
                queue.append(nx)  # 그 좌표를 큐에 추가하고
                graph[nx] = graph[x] + 1  # 그 전 좌표에 저장되어 있는 값에서 +1 한다.
                visited[nx] = x


graph = [0] * 100001  # 그래프 최대크기로 초기화
visited = [-1] * 100001  # 전에 방문했던 위치를 남길 visited선언
path = []  # 방문 기록을 담을 리스트 선언
dx = [-1, 1, 2]  # 한번에 이동 할 수 있는 좌표 설정

N, K = map(int, input().split())

print(bfs(N, K))  # 방문 횟수출력
print(*path[::-1])  # 방문 기록을 뒤에서 부터 출력
