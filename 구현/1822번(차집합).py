nA, nB = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A - B))  # 차집합의 길이를 출력
print(*sorted(list(A - B)))  # 차집합의 원소를 출력
