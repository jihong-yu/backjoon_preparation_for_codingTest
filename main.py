import itertools

N, M = map(int, input().split())
input_array = []
result = 0

for _ in range(N):
    input_array.append(list(map(int, input())))

bitmask = itertools.product([0, 1], repeat=N * M)


# 비트마스크를 N*M 행렬로 변환
def bitmask_converter(array):
    return [array[i:i + M] for i in range(0, len(array), M)]


for a in bitmask:
    # 비트마스크를 N*M 행렬로 변환
    bitmask_covert_array = bitmask_converter(a)

    # 가로합 저장
    sum_width = 0

    # 가로 계산
    for i in range(N):
        temp_width = 0
        for j in range(M):
            if bitmask_covert_array[i][j] == 0:
                temp_width = temp_width * 10 + input_array[i][j]
            if bitmask_covert_array[i][j] == 1 or j == M - 1:
                sum_width += temp_width
                temp_width = 0

    # 세로합 저장
    sum_height = 0

    # 세로 계산
    for i in range(M):
        temp_height = 0
        for j in range(N):
            if bitmask_covert_array[j][i] == 1:
                temp_height = temp_height * 10 + input_array[j][i]
            if bitmask_covert_array[j][i] == 0 or j == N - 1:
                sum_height += temp_height
                temp_height = 0

    result = max(result, sum_height + sum_width)

print(result)
