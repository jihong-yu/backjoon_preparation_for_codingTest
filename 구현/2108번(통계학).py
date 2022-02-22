import sys

# 입력 빠르게 받기
input = sys.stdin.readline

N = int(input())
sum_ = 0  # 합계저장

middle = 0
count_list = [0] * 8001
mode = 0
arr = []
for i in range(N):
    temp = int(input())

    # 전체합
    sum_ += temp

    # 입력받은 값을 리스트에 추가
    arr.append(temp)

    # 최빈값 구하기 위해 count 저장(음수도 저장하기 위해 4000씩 밀어주고 출력할때 빼준다.)
    count_list[temp + 4000] += 1

arr.sort()  # 정렬

# 최빈값 구하기
# 만약 최빈값이 두개이상이라면
if count_list.count(max(count_list)) > 1:
    mode_index = count_list.index(max(count_list))  # 첫번째 최빈값의 인덱스를 저장한 후
    # 첫번째 인덱스 이후에 있는 최빈값을 반환한다.
    mode = (count_list.index(max(count_list), mode_index + 1)) - 4000
# 만약 최빈값이 하나라면
else:
    mode = count_list.index(max(count_list)) - 4000  # 해당 최빈값을 추가

# 산술평균 구하기
# 만약 합계를 나눈 값이 -0.xxx 가나온다면
if -1 < sum_ / N <= 0:
    result = 0  # 해당 값을 0으로 바꿔준다.(-0으로 나오는 것을 방지)
else:  # 나머지 경우는 반올림 해준다.
    result = round(sum_ / N, 0)

print(f'{result :.0f}')  # 산술평균 출력
print(arr[N // 2])  # 중앙값 출력
print(mode)  # 최빈값 출력
print(arr[-1] - arr[0])  # 범위출력
