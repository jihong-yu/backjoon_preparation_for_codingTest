import sys

sys.setrecursionlimit(100001)

N = int(input())
array = [x for x in range(1, N + 1)]
input_array = list(map(int, input().split()))
visited = [False] * (N + 1)
out = []
result = -1


def solve(depth):
    global result
    if depth == N:

        if out == input_array and result == -1:
            print(-1)
            return
        if out == input_array and result != -1:
            print(' '.join(result))
            return
        result = [str(x) for x in out]

    for i in range(N, 0, -1):
        if not visited[i]:
            visited[i] = True
            out.append(i)
            solve(depth + 1)
            visited[i] = False
            out.pop()


solve(0)
