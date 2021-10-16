t = int(input())

array = [0, 1, 2, 4] # 1,2,3 일때 사용되는 횟수를 미리 배열에 선언

for i in range(4, 11): #문제에서 주어진 11까지 반복
    array.append(array[i - 3] + array[i - 2] + array[i - 1]) #i-3,i-2,i-1 번째에 있는 값들을 더한 값이 i번째에 등장한다.

for _ in range(t): #테스트 케이스 횟수만큼 돈다
    n = int(input())
    print(array[n])
