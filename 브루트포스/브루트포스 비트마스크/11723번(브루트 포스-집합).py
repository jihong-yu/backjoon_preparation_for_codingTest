import sys

input = sys.stdin.readline

S = set()

M = int(input())

for _ in range(M):
    input_operation = input().split()

    operation = input_operation[0]
    if len(input_operation) > 1:
        x = input_operation[1]

    if operation == 'add':
        S.add(x)
    elif operation == 'remove':
        if x in S:
            S.remove(x)
    elif operation == 'check':
        if x in S:
            print(1)
        else:
            print(0)
    elif operation == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif operation == 'all':
        S = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"}
    elif operation == 'empty':
        S.clear()
