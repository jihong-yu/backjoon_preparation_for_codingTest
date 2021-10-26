N, S = map(int, input().split())
array = list(map(int, input().split()))
count = 0  # 개수를 셀 count값 저장
out = []  # 재귀를 돌면서 위의 array에서 m개를 뽑아서 저장할 리스트 선언


def dfs(depth, idx, m):
    global count

    if depth == m:  # 만약 out 리스트에 m개만큼 추가되었다면
        if sum(out) == S:  # out리스트의 합이 S와 같다면
            count += 1  # count값 1증가
        return

    for i in range(idx, N):  # 인자로전달받은 idx부터 N까지 돈다.(이전에 돌았던 인덱스는 안돌기 위한 장치)
        out.append(array[i])  # out에 array배열의 값 한개를 추가
        dfs(depth + 1, i + 1, m)  # 그 후 또 dfs를 돈다.
        out.pop()  # 다돌앗으면 그 값을 out리스트에서 제거


# 입력받은 array리스트에서 j(1개~N개)의 개수만큼 원소를 뽑는다.
for j in range(1, N + 1):
    dfs(0, 0, j)

print(count)  # count값 출력
