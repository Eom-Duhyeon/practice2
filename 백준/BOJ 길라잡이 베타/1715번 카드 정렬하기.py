import heapq
import sys

n = int(sys.stdin.readline())
hp = []

for i in range(n):
    heapq.heappush(hp, int(sys.stdin.readline()))

answer = 0

while len(hp) != 1:
    a = heapq.heappop(hp)
    b = heapq.heappop(hp)
    c = a+b
    answer += c
    heapq.heappush(hp, c)

print(answer)