t = int(input())


def dfs(depth):
    global count

    if sum(out) > n:
        return

    if sum(out) == n:
        count += 1
        return

    for i in range(1, 4):
        out.append(i)
        dfs(depth + 1)
        out.pop()


for _ in range(t):
    n = int(input())
    count = 0
    out = []
    dfs(0)
    print(count)
