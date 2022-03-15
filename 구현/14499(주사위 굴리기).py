N, M, r, c, K = map(int, input().split())
maps = [list(map(int, input().split())) for i in range(N)]
direct = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]  # 주사위의 각면에 써있는 숫자
dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌

cur_bottom = 5  # 현재 바닥면

for dir in direct:

    if dir == 1:  # 동
        nr = r + dr[1]
        nc = c + dc[1]

        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue

        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]

    elif dir == 2:  # 서
        nr = r + dr[3]
        nc = c + dc[3]

        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue

        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]

    elif dir == 3:  # 북
        nr = r + dr[0]
        nc = c + dc[0]

        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue

        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

    else:  # 남
        nr = r + dr[2]
        nc = c + dc[2]

        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue

        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if maps[nr][nc] == 0:
        maps[nr][nc] = dice[cur_bottom]
    else:
        dice[cur_bottom] = maps[nr][nc]
        maps[nr][nc] = 0

    r, c = nr, nc
    print(dice[0])
