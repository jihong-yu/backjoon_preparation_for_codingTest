import sys

sys.setrecursionlimit(100000)

N, K = map(int, input().split())

array = [x for x in range(1, N + 1)]
result = []
index = 0  # 초기 index값 0


def move(index):
    # index가 0일때는 1번사람을 출력해야 하므로 index + 1을 해준다.
    # 만약 N이 7일 때 7번사람을 출력하기 위해서는 index가 0일때 이다.
    index = (index + 1) % N

    if array[index] != 0:  # 만약 아직 방문하지 않았다면
        return index  # 해당 index 반환
    else:  # 방문했다면
        return move(index)  # 그다음 인덱스로 넘어간다


for i in range(N):  # 총 N번 돌아야한다.
    for j in range(K):  # 무조건 K번 인덱스를 이동시켜야하기 때문에 K번 돈다.
        index = move(index)

    if index == 0:  # 만약 결과 index가 0이란건 7번째 사람을 뜻하므로
        result.append(N)  # N을 result에 넣어준다.

    else:  # 그 밖의 경우는 1~6 까지 이므로
        result.append(index)  # 그 값을 result값에 넣어준다.

    array[index] = 0

print('<' + ', '.join(map(str, result)) + '>')