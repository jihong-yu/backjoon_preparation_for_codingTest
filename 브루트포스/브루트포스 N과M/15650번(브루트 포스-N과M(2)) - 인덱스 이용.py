n, m = map(int, input().split())

out = []
visited = [False] * (n + 1)


def solve(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, n + 1):
        if not visited[i]:
            visited[i] = True
            out.append(i)
            solve(depth + 1, i + 1, n, m)
            visited[i] = False
            out.pop()


solve(0, 1, n, m)
