n, m = map(int, input().split())

array = [x for x in range(1, n + 1)]
result = []
out = []
visited = [False] * n


def solve(depth, n, m):
    if depth == m:
        out_str = sorted(out)  # out값들을 정렬해서 out_str 리스트에 넣는다.
        if out_str not in result:  # 만약 result에 out_str값이 존재하지 않는다면
            result.append(out_str)  # 그 값을 result에 추가
        return
    for i in range(depth, n):
        if not visited[i]:
            visited[i] = True
            out.append(i + 1)
            solve(depth + 1, n, m)
            visited[i] = False
            out.pop()


solve(0, n, m)

for i in result:
    print(' '.join(map(str, i)))
