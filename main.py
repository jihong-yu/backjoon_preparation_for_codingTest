import sys
from collections import deque


graph = []

N, M = map(int, input().split())

for _ in range(N):
    a = list(map(int, input().split()))
    graph.append(a)

print(graph)
