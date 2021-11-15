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

    if y == "push":
        q.append(x)
    elif y == "pop":
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif y == "size":
        print(len(q))
    elif y == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif y == "front":
        if len(q) > 0:
            print(q.__getitem__(0))
        else:
            print(-1)
    elif y == "back":
        if len(q) > 0:
            print(q.__getitem__(len(q)-1))
        else:
            print(-1)