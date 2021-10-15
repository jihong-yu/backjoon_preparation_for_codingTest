n = int(input())

input_len = len(str(n))

remoteNum = [x for x in range(10)]
currentChannel = 100
breakdownButtonNum = int(input())

#만약 고장난 버튼이 0개 이상이라면
if breakdownButtonNum > 0:
    breakdownButtons = list(map(int, input().split()))
    # 고장난 리모컨 버튼 제거
    for i in breakdownButtons:
        remoteNum.remove(i)

#우선 현재 채널과 입력받은 채널의 차의 절대값을 결과를 출력할 변수에 대입
result = abs(currentChannel - n)

#0번부터 999999번까지 채널을 순회한다.(999999까지 도는이유는 만약 버튼을 8,9만 눌릴수 있다고 쳤을 때 500000채널까지 가기위해서는
#99999 에서 가는것보다 888888에서 내려가는 것이 더가깝기 때문이다.)
for channel in range(1000000):
    for j in range(len(str(channel))): #각 채널을 문자열로 변환해서 그 길이만큼 돈다.
        if int(str(channel)[j]) not in remoteNum: #만약 채널의 각각의 자리수가 리모컨의 고장나 있는 버튼이라면
            break #해당 반복문 탈출(고장난 버튼이 포함되어있는 채널)
        elif len(str(channel)) - 1 == j: #만약 해당채널의 마지막 자리수까지 위에서 검사를 했다면
            result = min(result, len(str(channel)) + abs(channel - n)) #우선 해당 채널에서 입력받은 채널까지 버튼을 눌리는 총 횟수와 기존의 100번부터
            #입력받은 채널을 +- 로 이동하는 횟수와 비교해서 최솟값을 대입 -> 그 후 채널마다 계속해서 더 작은 값을 결과값에 대입

print(result)
