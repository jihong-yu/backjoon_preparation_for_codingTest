N = int(input())
array = [[0, 0]]
for _ in range(N):
    T, P = map(int, input().split())
    array.append([T, P])

result = 0


def solve(day, sum_):
    global result
    if day == N + 1:
        result = max(result, sum_)
        return
    if day > N + 1:
        return

    solve(array[day][0] + day, sum_ + array[day][1])

    solve(day + 1, sum_)


solve(1, 0)
print(result)
