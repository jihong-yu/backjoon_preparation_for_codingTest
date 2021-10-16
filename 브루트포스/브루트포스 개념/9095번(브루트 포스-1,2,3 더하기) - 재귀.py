def solve(n):
    global cnt
    global k
    for i in arr:
        res.append(i)
        if sum(res) == n:
            res.pop()
            cnt += 1
            break
        solve(n)
        res.pop()
    return cnt


T = int(input())
for _ in range(T):
    n = int(input())
    arr = [1, 2, 3]
    res = []
    cnt = 0
    print(solve(n))
