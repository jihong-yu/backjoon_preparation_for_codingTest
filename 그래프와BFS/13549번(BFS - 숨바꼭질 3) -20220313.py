from collections import deque


def bfs(start):
    queue = deque([[start, 0]])
    while queue:

        x, cnt = queue.popleft()

        # find 함수 (자기 노드의 부모를 찾아가는 함수)
        if x == K:
            return cnt  # 본인의 노드까지 리스트에 넣어 반환

        for i in range(3)[::-1]:
            if i != 2:
                nx = x + dx[i]
            else:
                nx = x * dx[i]

            # nx가 범위를 벗어나지 않고 방문을 안했고 출발지가 아니라면
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True  # 방문처리
                if i != 2:
                    queue.append([nx, cnt + 1])
                else:  # 순간이동한다면 초 추가 없이 큐에 넣어준다.
                    queue.appendleft([nx, cnt])


N, K = map(int, input().split())

dx = [-1, 1, 2]  # 이동방향 처리
visited = [False] * 100001  # 방문처리할 리스트

cnt = bfs(N)
print(cnt)
