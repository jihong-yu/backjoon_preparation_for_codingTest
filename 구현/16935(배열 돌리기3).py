N, M, R = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]

oper_cnt = list(map(int, input().split()))

for order in range(R):

    if oper_cnt[order] == 1:

        for i in range(N // 2):
            array[i][:], array[-(i + 1)][:] = array[-(i + 1)][:], array[i][:]

    elif oper_cnt[order] == 2:

        for i in range(N):
            for j in range(M // 2):
                array[i][j], array[i][-(j + 1)] = array[i][-(j + 1)], array[i][j]

    elif oper_cnt[order] == 3:
        temp = list(zip(*(array[::-1])))
        array = [[] for _ in range(len(temp))]
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                array[i].append(temp[i][j])

        N, M = len(array), len(array[0])

    elif oper_cnt[order] == 4:
        temp = list(zip(*array))[::-1]
        array = [[] for _ in range(len(temp))]
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                array[i].append(temp[i][j])

        N, M = len(array), len(array[0])

    elif oper_cnt[order] == 5 or oper_cnt[order] == 6:
        temp_array2 = []
        for i in range(N):
            temp = []
            for j in range(M):
                temp.append(array[i][j])
            temp_array2.append(temp)

        if oper_cnt[order] == 5:
            for i in range(N):
                for j in range(M):
                    if i < N // 2 and j < M // 2:
                        temp_array2[i][j + M // 2] = array[i][j]
                    elif i < N // 2 and j >= M // 2:
                        temp_array2[i + N // 2][j] = array[i][j]
                    elif i >= N // 2 and j >= M // 2:
                        temp_array2[i][j - M // 2] = array[i][j]
                    else:
                        temp_array2[i - N // 2][j] = array[i][j]

        elif oper_cnt[order] == 6:

            for i in range(N):
                for j in range(M):
                    if i < N // 2 and j < M // 2:
                        temp_array2[i + N // 2][j] = array[i][j]
                    elif i < N // 2 and j >= M // 2:
                        temp_array2[i][j - M // 2] = array[i][j]
                    elif i >= N // 2 and j >= M // 2:
                        temp_array2[i - N // 2][j] = array[i][j]
                    else:
                        temp_array2[i][j + M // 2] = array[i][j]

        array = temp_array2

for i in range(N):
    print(*array[i])
