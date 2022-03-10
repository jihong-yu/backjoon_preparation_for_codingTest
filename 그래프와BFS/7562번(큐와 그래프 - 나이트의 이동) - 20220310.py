import sys
from collections import deque


input = sys.stdin.readline

def bfs(cr, cc):
    queue = deque([[cr, cc]])

    while queue:
        r, c = queue.popleft()

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr >= I or nr < 0 or nc >= I or nc < 0 or array[nr][nc] != 0:
                continue

            array[nr][nc] = array[r][c] + 1
            if nr == fr and nc == fc:
                return
            queue.append([nr, nc])


dr = [-1, -2, -2, -1, 1, 2, 2, 1]  # 좌상, 우상, 우하, 좌하
dc = [-2, -1, 1, 2, 2, 1, -1, -2]  # 좌상, 우상, 우하, 좌하

T = int(input())

for _ in range(T):
    I = int(input())
    cr, cc = map(int, input().split())
    fr, fc = map(int, input().split())

    array = [[0] * I for _ in range(I)]

    if cc != fr or cc != fc:
        bfs(cr, cc)
    print(array[fr][fc])
