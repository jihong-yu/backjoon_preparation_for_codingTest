N, K, A, B = map(int, input().split())

list_ = [K] * N
count = 0
while True:

    count += 1

    for i in range(len(list_)):
        list_[i] -= 1

    index_ = list_.index(min(list_))

    for i in range(index_,index_ + A):
        list_[i] += B

    if list_.count(0) >= 1:
        break

print(count)
