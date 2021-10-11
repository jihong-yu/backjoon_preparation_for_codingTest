n = int(input())

sum_ = 0
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if i % j == 0:
#             sum_ += j

for i in range(1, n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            sum_ += j
            if i // j != j:  # 예를 들어 i가 25일 경우 5가 두번 들어가는 것을 방지
                sum_ += (i // j)
print(sum_)
