import itertools

array = []
for i in range(9):
    array.append(int(input()))

array2 = []

for i in itertools.combinations(array, 7):
    if sum(i) == 100:
        for j in i:
            array2.append(j)
        break

array2.sort()

for i in array2:
    print(i)
