import sys

input = sys.stdin.readline

n = int(input())
input_array = [0]

for _ in range(n):
    input_array.append(list(map(int, input().split())))

for i in range(2, n + 1):
    for j in range(len(input_array[i])):
        if j == 0:  # 인덱스가 0일 때는 -1의 인덱스가 없기 때문에 비교할 필요 없다.
            input_array[i][j] = input_array[i][j] + input_array[i - 1][j]
        elif j == len(input_array[i]) - 1:  # 인덱스가 마지막일 때도 비교할 필요 없다.
            input_array[i][j] = input_array[i - 1][j - 1] + input_array[i][j]
        else:  # 그 외의 경우 그전 행의 왼쪽위 숫자와 오른쪽 위 숫자중 큰 값을 들고와야 하기 때문에 max값으로 비교 
            input_array[i][j] = max(input_array[i - 1][j] + input_array[i][j],
                                    input_array[i - 1][j - 1] + input_array[i][j])

print(max(input_array[n]))  # 마지막 행 중 가장 큰 값
