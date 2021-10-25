import sys

N = int(input())
travel_cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_value = sys.maxsize


def dfs(start, next, value, visited):
    global min_value

    if len(visited) == N:
        if travel_cost[next][start] != 0:
            min_value = min(min_value, value + travel_cost[next][start])
        return

    for i in range(N):
        if travel_cost[next][i] != 0 and i != start and i not in visited and value < min_value:
            visited.append(i)
            dfs(start, i, value + travel_cost[next][i], visited)
            visited.pop()


# 각 번호에서 시작
for i in range(N):
    dfs(i, i, 0, [i])

print(min_value)
