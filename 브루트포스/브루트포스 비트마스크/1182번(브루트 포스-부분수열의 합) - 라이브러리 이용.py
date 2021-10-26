import itertools

N, S = map(int, input().split())
array = list(map(int, input().split()))
count = 0

for i in range(1, N + 1):
    for j in itertools.combinations(array, i):
        if sum(j) == S:
            count += 1

print(count)
