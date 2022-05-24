import heapq
import sys

n = int(input())
hp = []
for i in range(n):
    heapq.heappush(hp, int(sys.stdin.readline()))

for i in range(n):
    print(heapq.heappop(hp))