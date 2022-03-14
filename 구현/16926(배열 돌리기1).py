N, M, R = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]

for order in range(R):
    top = N
    left = 0
    right = M
    bottom = 0

    for _ in range(min(N, M) // 2):
        temp = 0  # 대입되어질 자리의 수를 저장해놓는 변수1
        temp2 = 0  # 대입되어질 자리의 수를 저장해놓는 변수2
        # top(윗줄 처리)
        for t in range(right - 1, left, -1):
            if temp != 0:  # 만약 temp가 0이아니라면
                temp2 = array[bottom][t - 1]  # 대입되어질 자리의 수를 2번째 변수에 저장해놓는다.
                array[bottom][t - 1] = temp  # 저장되어있는 수를 대입한다.
                temp = temp2  # 저장된 수를 바꿔준다.
            else:  # 0이라면 음이므로
                temp = array[bottom][t - 1]  # temp값에 대입되어질 수를 저장해놓는다.
                array[bottom][t - 1] = array[bottom][t]  # 그 자리에 대입한다.

        # left (왼쪽줄 처리)
        for l in range(bottom, top - 1):
            temp2 = array[l + 1][left]  # 대입되어질 자리의 수를 2번째 변수에 저장
            array[l + 1][left] = temp  # 위에서 넘어온 temp값을 그대로 그 자리에 저장
            temp = temp2  # 저장된 수를 변경
        # bottom (밑줄 처리)
        for b in range(left, right - 1):
            temp2 = array[top - 1][b + 1]
            array[top - 1][b + 1] = temp
            temp = temp2
        # right(오른쪽 줄 처리)
        for r in range(top - 1, bottom, -1):
            temp2 = array[r - 1][right - 1]
            array[r - 1][right - 1] = temp
            temp = temp2

        # 각각의 범위를 한칸씩 줄여준다.(즉,한칸 안으로 들어와 사각형을 검사)
        top -= 1
        left += 1
        right -= 1
        bottom += 1

for i in range(N):
    print(*array[i])
