n = int(input())

dp = [0, 1, 3]  # n이 2이하일때 횟수를 미리 초기화

if n > 2:
    for i in range(3, n + 1):
        dp = dp + [0] * (n - 2)
        dp[i] = (dp[i - 2] * 2) + dp[i - 1]

print(dp[n] % 10007)
