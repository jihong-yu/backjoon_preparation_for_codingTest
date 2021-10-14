e, s, m = map(int, input().split())

arrayE = [x for x in range(1, 16)]
arrayS = [x for x in range(1, 29)]
arrayM = [x for x in range(1, 20)]
i = 0
while True:
    if arrayE[i % 15] == e and arrayS[i % 28] == s and arrayM[i % 19] == m:
        print(i+1)
        break
    i += 1
