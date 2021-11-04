N = int(input())

input_array = list(map(int, input().split()))
dp = [input_array[0]] * N

for i in range(1, N):
    dp[i] = max(dp[i - 1] + input_array[i], input_array[i])

print(max(dp))
