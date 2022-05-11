"""
2 1
5 10
100 100
11
"""


import heapq
import sys

n, k = map(int, input().split())
gems = []
bags = []
possible = []
total = 0
for i in range(n):
    weight, value = map(int, sys.stdin.readline().split())
    heapq.heappush(gems, (weight, value))

for i in range(k):
    heapq.heappush(bags, int(sys.stdin.readline()))

for i in range(k):
    current = heapq.heappop(bags)
    while gems and current >= gems[0][0]:
        w, v = heapq.heappop(gems)
        heapq.heappush(possible, -v)

    if possible:
        total -= heapq.heappop(possible)
    elif not gems: # 후보군도 없고 보석도 없음
        break

print(total)

