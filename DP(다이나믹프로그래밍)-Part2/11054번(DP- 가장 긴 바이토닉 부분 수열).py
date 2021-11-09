import sys

input = sys.stdin.readline

N = int(input())
input_array = list(map(int, input().split()))
dp_increase = [1] * N  # 증가하는 부분수열

# 뒤에서부터 증가하는 부분수열을 구하기위해 배열을 반대방향으로 돌린다.
reversed_input_array = list(reversed(input_array))
dp_decrease = [1] * N  # 뒤에서 증가하는 부분수열(정방향으로는 감소하는 부분수열)

for i in range(N):
    for j in range(i):
        if input_array[i] > input_array[j]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)
        if reversed_input_array[i] > reversed_input_array[j]:
            dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)

result = []
for i in range(N):
    result.append(dp_increase[i] + dp_decrease[N - i - 1] - 1)

print(max(result))

