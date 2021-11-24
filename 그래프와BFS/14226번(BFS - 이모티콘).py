from collections import deque


def bfs():
    queue = deque()
    queue.append([1, 0])  # 화면 이모티콘 개수,클립보드 이모티콘 개수
    graph[1][0] = 0  # 화면이모티콘이1개이고 클립보드 이모티콘 개수가 0일때는 초기 값이므로 0으로 세팅

    while queue:
        s, c = queue.popleft()

        if graph[s][s] == -1:  # 방문하지않았다면
            graph[s][s] = graph[s][c] + 1  # 화면에 있는 이모티콘 클립보드에 붙여넣기
            queue.append([s, s])

        if s + c < 1001 and graph[s + c][c] == -1:  # s+c가 그래프의 범위를 넘지 않고 방문하지 않았다면
            graph[s + c][c] = graph[s][c] + 1  # 클립보드에 있는 이모티콘 화면에 붙여넣기
            queue.append([s + c, c])

        if graph[s - 1][c] == -1 and s - 1 >= 0:  # s - 1 이 그래프의 범위를 넘지 않고 방문하지 않았다면
            graph[s - 1][c] = graph[s][c] + 1  # 화면에 있는 이모티콘 개수 -1
            queue.append([s - 1, c])


S = int(input())
graph = [[-1] * 1001 for _ in range(1001)]  # 그래프의 최대 범위만큼 설정
result = -1  # 정답을 출력할 result값 선언

bfs()  # bfs 실행

for i in range(S + 1):  # 원하는 이모티콘 개수를 출력할때 까지 반복문 실행
    if graph[S][i] != -1:  # 만약 그래프에 저장되어있는 횟수가 -1 즉, 만들수 없는 횟수가 아닌경우
        if result == -1 or result > graph[S][i]:  # result값이 -1 이거나 저장되어있는 result 값이 그래프의 특정 횟수보다 클경우
            result = graph[S][i]  # 그 횟수를 더 작은 횟수로 바꾸어 준다

print(result)