import sys

N = int(input())
P = [0] + list(map(int, input().split()))
dp = [x for x in P]

for i in range(2, N + 1):
    for j in range(1, i + 1):
        if dp[i] > dp[i - j] + P[j]:
            dp[i] = dp[i - j] + P[j]
        # dp[i] = min(dp[i], dp[i - j] + P[j])

print(dp[N])
