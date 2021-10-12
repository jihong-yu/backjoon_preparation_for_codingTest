import sys

questionRange = 1000000 #문제에서 주어진 n의 범위
array = [True] * (questionRange + 1) #소수를 저장할 리스트를 n의범위+1 만큼 선언 및 초기화
array[0], array[1] = False, False #0,1은 소수가 아니기에 False로 초기화

#에라토스테네스의체 공식으로 소수 구하기
for i in range(2, int(len(array) ** 0.5) + 1): #주어진범위의 제곱근까지만 돌기
    j = 2 # 각 인덱스 i에 곱할 j 선언
    while True:
        if array[i]: #만약 리스트의 인덱스가 True라면(소수라면)
            array[i * j] = False #그의 배수들은 모두 소수가 아니게 된다.
            j += 1 #j값 증가
            if i * j >= len(array): #만약 j가 계속해서 증가하다가 배열의 길이보다 같거나 커진다면
                break #반복문 탈출
        else: #만약 리스트의 인덱스가 False라면(소수가 아니라면) <- 소수가 아니라는 소리는 이미 앞에서 해당 배수를 다 False로 처리했기 때문에
            break #반복문 탈출

while True: #무한반복
    n = int(sys.stdin.readline()) #n을 입력받는다.
    if n == 0: break #만약 n이 0라면 반복문탈출
    resultA, resultB = 0, (questionRange + 1) #초기 reusltA,resultB의 값에다 A는 0 B는 문제에서 주어진 범위보다 큰 값을 대입
    a = 0 #a를 0으로 초기화
    b = n #b를 0을 초기화
    while True:
        if array[a] and array[b]: #만약 a,b가 모두 소수라면
            resultA = a #그 값을 resultA값에 대입
            resultB = b #그 값을 resultB값에 대입
            break #반복문 탈출
        a += 1 #소수가 아니라면 a는 1씩증가
        b -= 1 #b는 1씩 감소
    if resultA != 0 and resultB != (questionRange + 1): #resultA,resultB의 값이 초기값과 다르다면
        print(f'{n} = {resultA} + {resultB}') #그 값을 출력
    else: #초기값과 같다면
        print("Goldbach's conjecture is wrong.")
