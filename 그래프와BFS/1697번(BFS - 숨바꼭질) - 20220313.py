from collections import deque


def bfs(start):
    global result

    queue = deque([[start, 0]])

    while queue:

        x, cnt = queue.popleft()

        if x == K:
            return cnt

        for i in range(3):
            if i != 2:
                nx = x + dx[i]
            else:
                nx = x * dx[i]

            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                queue.append([nx, cnt + 1])


N, K = map(int, input().split())

dx = [-1, 1, 2]
visited = [False] * 100001

result = 0

print(bfs(N))

