import sys


def solve(dp):
    dp = dp + [0] * (n - 2)
    if n > 3:
        for i in range(4, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    return dp[n]


T = int(input())
for _ in range(T):
    dp = [0, 1, 2, 4]
    n = int(sys.stdin.readline())
    print(solve(dp))
