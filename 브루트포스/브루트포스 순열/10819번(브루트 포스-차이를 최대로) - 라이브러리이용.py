import itertools

N = int(input())

input_array = list(map(int, input().split()))
result = 0 #결과 값을 저장할 result 값 선언


def result_solve(array):  # 리스트의 차를 구하는 공식
    global result

    def_result = 0 #각 원소의 차를 저장
    for i in range(len(array) - 1):
        def_result += abs(array[i] - array[i + 1]) #각 원소의 차의 절대값을 계속해서 더해나간다.
    result = max(result, def_result) #저장되어있는 결과값과 비교해서 큰 값을 결과값에 대입


for i in itertools.permutations(input_array, N): #permutations라이브러리 이용(입력받은 리스트의 원소중에서 N개를 뽑는다.)
    result_solve(i) #뽑은 순열마다 리스트의 차를 구하여 result에 대입

print(result)
