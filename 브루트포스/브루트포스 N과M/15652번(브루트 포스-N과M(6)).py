n, m = map(int, input().split())
array = [int(x) for x in input().split()]
array.sort()  # 오름차순으로 출력하기 위해 정렬
visited = [False] * (max(array) + 1)  # 방문했는지 확인을 위한 리스트
out = []  # 출력을 위한 리스트


def solve(depth, idx, n, m):
    if depth == m:
        print(' '.join(out))
        return
    for i in range(idx, len(array)):  # 입력받은 배열의 원소를 돈다
        if not visited[i]:  # 만약 해당 원소가 방문하지 않았다면
            visited[i] = True  # 방문한 것으로 바꿔주고
            out.append(str(array[i]))  # 그 값을 추가
            solve(depth + 1, i + 1, n, m)  # 다시 깊이+1 해준다음 다시 돈다.
            visited[i] = False  # 다 돌았으면 방문안한것으로 False
            out.pop()  # 그 값을 지워준다.


solve(0, 0, n, m)
