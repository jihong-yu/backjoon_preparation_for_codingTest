n, m = map(int, input().split())
out = []


def solve(depth, idx, n, m):
    if depth == m:
        print(' '.join(out))
        return
    for i in range(idx, n + 1):
        out.append(str(i))
        solve(depth + 1, i, n, m)
        out.pop()


solve(0, 1, n, m)