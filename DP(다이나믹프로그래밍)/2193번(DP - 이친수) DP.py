N = int(input())

dp = [1 for _ in range(N + 1)]

for i in range(3, N + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[N])
