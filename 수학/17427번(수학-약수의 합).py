n = int(input())

sum_ = 0
for i in range(1, n + 1):
    # 1부터 n 범위내에서 i의 배수의 개수 = 1부터 n의 범위내에서 i를 약수로 가지는 개수(n을 i로 나눈 몫)
    # 예를들면 1부터 100 까지 11의 배수의 개수는 11,22,33...99 까지 9개 = (100 // 11)
    sum_ += (n // i) * i

print(sum_)
