k = int(input())

sign = list(map(str, input().split()))
visited = [False] * (11)
maxResult = ""
minResult = ""


def possible(i, j, sign):
    if sign == '<':
        return i < j
    else:
        return i > j


def solve(depth, s):
    global maxResult, minResult
    if depth == k + 1:
        if len(minResult) == 0:
            minResult = s
        else:
            maxResult = s
        return

    for i in range(10):
        if not visited[i]:
            print(s)
            if depth == 0 or possible(s[len(s)-1], str(i), sign[depth - 1]):
                visited[i] = True
                solve(depth + 1, s + str(i))
                visited[i] = False


solve(0, "")
print(maxResult)
print(minResult)
