import sys

sys.setrecursionlimit(100001)

def solve(n):
    global cnt

    for i in arr:
        res.append(i)
        print(res)
        if sum(res) == n:
            cnt += 1
            res.pop()
            return
        solve(n)
        res.pop()


t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    res = []
    arr = [1, 2, 3]
    solve(n)
    print(cnt)
