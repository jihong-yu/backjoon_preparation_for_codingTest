import sys

input = sys.stdin.readline

N = int(input())
cost = [[0, 0, 0]]
for _ in range(N):
    cost.append(list(map(int, input().split())))

dp = [i for i in cost]

for i in range(2, N + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
    dp[i][1] = min(dp[i - 1][2], dp[i - 1][0]) + dp[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]

print(min(dp[N]))
