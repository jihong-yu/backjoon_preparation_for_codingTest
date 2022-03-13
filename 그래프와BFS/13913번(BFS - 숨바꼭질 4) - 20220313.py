from collections import deque


def bfs(start):
    queue = deque([[start, 0]])
    while queue:

        x, cnt = queue.popleft()

        # find 함수 (자기 노드의 부모를 찾아가는 함수)
        if x == K:
            arr = []
            while x != parent_node[x]:  # 만약 자신의 부모가 최상위 부모가 아니라면 반복문돌기
                arr.append(parent_node[x])  # 우선 부모의 길을 저장해주고
                x = parent_node[x]  # 부모를 저장해준다.

            return cnt, [K] + arr  # 본인의 노드까지 리스트에 넣어 반환

        for i in range(3):
            if i != 2:
                nx = x + dx[i]
            else:
                nx = x * dx[i]

            # nx가 범위를 벗어나지 않고 방문을 안했고 출발지가 아니라면
            if 0 <= nx <= 100000 and not visited[nx] and nx != start:
                visited[nx] = True
                queue.append([nx, cnt + 1])
                parent_node[nx] = x


N, K = map(int, input().split())

dx = [-1, 1, 2]  # 이동방향 처리
visited = [False] * 100001  # 방문처리할 리스트
parent_node = [i for i in range(100001)]  # 자신의 부모노드를 저장할 리스트

cnt, arr = bfs(N)
print(cnt)
print(*arr[::-1])
