# n+1일째 되는 날 퇴사
n = int(input())
t = [0] * (n + 1)
p = [0] * (n + 1)

answer = 0

for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())


def go(day, sum_):
    global answer

    # 종료조건: 퇴사날에 딱 맞췄을 때
    if day == n + 1:
        answer = max(sum_, answer)
        return

    # 불가능한 경우: 상담을 했을 때, 퇴사날을 넘어가는 경우
    if day > n + 1:
        return

    # 상담을 한다
    go(day + t[day], sum_ + p[day])

    # 상담을 안한다
    go(day + 1, sum_)


go(1, 0)
print(answer)
