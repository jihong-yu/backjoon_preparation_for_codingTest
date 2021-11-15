import sys
from collections import deque

input = sys.stdin.readline
q = deque([])

n = int(input())

for _ in range(n):
    user_input = list(map(str, input().split()))
    y = user_input[0]

    if len(user_input) > 1:
        x = int(user_input[1])
    if y == "push_front":
        q.appendleft(x)
    elif y == "push_back":
        q.append(x)
    elif y == "pop_front":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif y == "pop_back":
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif y == "size":
        print(len(q))
    elif y == "empty":
        if len(q) > 0:
            print(0)
        else:
            print(1)
    elif y == "front":
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif y == "back":
        if len(q) > 0:
            print(q[len(q)-1])
        else:
            print(-1)