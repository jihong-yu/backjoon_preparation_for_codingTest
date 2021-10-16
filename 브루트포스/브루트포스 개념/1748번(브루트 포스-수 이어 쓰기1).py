n = int(input())
result = 0 #결과값 출력을 위한 변수

plusNum = "9" #더해줄 값을 9로 선언
minusNum = "" #빼줄 값을 빈 문자열로 선언

if len(str(n)) > 1: #만약 길이가 1이상이라면
    for i in range(1,len(str(n))+1): #입력받은 수의 길이만큼 돈다
        if i != len(str(n)): #만약 입력받은 str의 길이가 i랑 같지 않다면
            result += (i * int(plusNum)) #result값에 i값과 plusnum(9,90,900.....) 곱한 값을 더해준다.
        elif i == len(str(n)): #만약 i가 n의 길이에 도달했다면
            result += ((n - int(minusNum)) * i) #result값은 (입력받은 수에서 minusnum(9,99,999...)를 빼준다.)
        minusNum += "9" #minusNum에 9를 계속 추가
        plusNum += "0" #plusnum에는 0을 추가
else: #길이가 1이라면
    result = n #n값을 결과값에 대입

print(result)