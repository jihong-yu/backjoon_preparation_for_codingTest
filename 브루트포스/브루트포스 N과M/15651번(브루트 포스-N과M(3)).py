n, m = map(int, input().split())
out = []


def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in range(1, n + 1):
        out.append(i)
        solve(depth + 1, n, m)
        out.pop()


solve(0, n, m)
