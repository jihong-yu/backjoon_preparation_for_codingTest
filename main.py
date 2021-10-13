n = int(input())
array = [list(input()) for i in range(n)]
maxCount = 0 #사탕의 최대 개수

def countFunc():
    global maxCount

    for i in range(n):
        countRow = 1
        countColumn = 1
        for j in range(n-1):
            #행 처리
            if array[i][j] == array[i][j - 1]:
                countRow += 1
            else:
                if maxCount < countRow:
                    maxCount = countRow
                countRow = 1

            #열 처리
            if array[j][i] == array[j + 1][i]:
                countColumn += 1
            else:
                if maxCount < countColumn:
                    maxCount = countColumn
                countColumn = 1

        if maxCount < countColumn:
            maxCount = countColumn

        if maxCount < countRow:
            maxCount = countRow

#행처리
for i in range(n):
    for j in range(1, n):
        array[i][j], array[i][j - 1] = array[i][j - 1], array[i][j]  # 사탕 교환
        countFunc()
        array[i][j], array[i][j - 1] = array[i][j - 1], array[i][j]  # 교환한 것을 원래대로
        
#열처리
for i in range(n):
    for j in range(1, n):
        array[j][i], array[j - 1][i] = array[j - 1][i], array[j][i]  # 사탕 교환
        countFunc()
        array[j][i], array[j - 1][i] = array[j - 1][i], array[j][i]  # 교환한 것을 원래대로

print(maxCount)