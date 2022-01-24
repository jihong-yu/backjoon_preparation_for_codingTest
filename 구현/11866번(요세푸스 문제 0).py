from collections import deque

N, K = map(int, input().split())
K = K - 1
array = [x for x in range(1, N + 1)]
yosepoose = []  # 출력할 요세푸스 배열 선언

queue = deque(array)

while True:

    for i in range(K):  # k - 1 번째 까지 돈다.
        queue.append(queue.popleft())  # 큐의 맨 앞의 원소를 큐의 맨뒤로 순서대로 보낸다.
    yosepoose.append(queue.popleft())  # 출력할 리스트에 맨앞 원소부터 넣어 준다.

    if len(yosepoose) == len(array):  # 만약 요세푸스 원소의 길이가 입력받은 배열의 길이와 같아졌다면 반복문 탈출
        break

print('<' + ', '.join(map(str, yosepoose)) + '>')
