import sys
from collections import deque

input = sys.stdin.readline


N, K = map(int, input().split())


def bfs(startX, destY):  # 시작점, #목적지
    queue = deque()  # BFS를 위한 큐 선언
    queue.append(startX)  # 시작점 추가
    graph[startX] = 0  # 시작점의 값을 0으로 초기화
    while queue:  # 큐를 돈다.
        x = queue.popleft()  # 큐의 첫번째 값을 뺀다.

        if x == destY:  # 해당 값이 목적지라면
            return graph[x]  # 그 값에 저장되어 있는 횟수를 리턴

        for i in range(3):  # 반복문을 3번 돈다.
            if i != 0:  # 만약 0이 아니라면
                nx = x + dx[i]  # +1, -1
            else:  # 만약 0이라면
                nx = x * dx[i]  # *2

            if nx < 0 or nx >= len(graph):  # 만약 그래프의 범위를 벗어난다면
                continue  # 아래의 코드 실행x

            if i != 0:  # 만약 i가 0이 아니라면(+1,-1라면)
                if graph[nx] == -1:  # 아직 방문하지 않은 점이라면
                    queue.append(nx)  # 그 값을 큐에 추가
                    graph[nx] = graph[x] + 1  # 1초가 걸리기 때문에 전의 횟수에 +1

            else:  # 만약 i가 0이라면(즉, *2라면)
                if graph[nx] == -1:  # 아직 방문하지 않은 점이라면
                    queue.append(nx)  # 그 값을 큐에 추가
                    graph[nx] = graph[x]  # 0초이기 때문에 전에 횟수를 그대로 추가.


graph = [-1] * 100001  # 그래프를 -1로 초기화
dx = [2, -1, 1]  # 이동할 수 있는 위치 선언

print(bfs(N, K))
