import sys

input = sys.stdin.readline

N = int(input())
dp = [[1, 1, 1] for _ in range(N + 1)]

for i in range(2, N + 1):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][1] + dp[i - 1][0] + dp[i-1][2]) % 9901

print(sum(dp[N]) % 9901)
