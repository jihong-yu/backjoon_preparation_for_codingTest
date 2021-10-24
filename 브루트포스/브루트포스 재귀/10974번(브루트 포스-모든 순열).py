import sys

sys.setrecursionlimit(100001)  # 재귀 횟수 제한 해제

N = int(input())
input_array = [x for x in range(1, N + 1)]  # 1~N까지 선언
result_array = sorted(input_array, reverse=True)  # 재귀 탈출을 위해 모든 순열 마지막 인자를 선언


def solve(def_array):
    print(*def_array)  # 리스트 출력
    if def_array == result_array:  # 만약 순열과 모든순열의 마지막 순열이 같다면
        exit()  # 코드 종료
    for i in range(N - 1, 0, -1):  # 마지막 항부터 돈다
        if def_array[i - 1] < def_array[i]:  # 만약 앞 열의 값이 그 뒷열의 값보다 작다면
            for j in range(N - 1, 0, -1):  # 다시 그 앞 열의 값을 맨 뒷열부터 비교
                if def_array[i - 1] < def_array[j]:  # 그 앞열의 값이 뒤에 있는 어느 열보다 작다면
                    def_array[i - 1], def_array[j] = def_array[j], def_array[i - 1]  # 그 두 값을 스왑
                    def_array = def_array[:i] + sorted(def_array[i:])  # i-1 번째 까지의 리스트와 그 뒤에리스트를 정렬한 채로 붙인다.
                    solve(def_array)  # 이 과정을 반복


solve(input_array)
