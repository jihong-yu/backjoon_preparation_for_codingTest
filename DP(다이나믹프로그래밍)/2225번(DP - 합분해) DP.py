N, K = map(int, input().split())

# 모든 값을 1로 초기화한다.(K가 1일때 N의 값과 관계없이 개수는 1개이기 때문)
dp = [[1] * (K + 1) for _ in range(N + 1)]

# N이 1일 때의 개수는 K값과 동일하기 때문에 K값으로 초기화
for a in range(1, K + 1):
    dp[1][a] = a

# N,K를 2부터 돌아준다.(점화식이 N,K >=2 일때부터 성립하기 때문)
for i in range(2, N + 1):
    for j in range(2, K + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[N][K] % 1000000000)
