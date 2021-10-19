import itertools

n, m = map(int, input().split())

array = [x for x in range(1, n + 1)]

for i in itertools.permutations(array, m):
    print(' '.join(map(str, i)))
