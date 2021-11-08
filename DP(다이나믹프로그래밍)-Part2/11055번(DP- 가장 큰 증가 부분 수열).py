import sys

input = sys.stdin.readline

N = int(input())
input_array = list(map(int, input().split()))
dp = [input_array[0]] * N


# 각 원소마다 몇번째로 증가하는 수인지 dp에 저장
for i in range(N):
    for j in range(i):
        if input_array[i] > input_array[j]:
            dp[i] = max(dp[i], dp[j] + input_array[i])

print(max(dp))

