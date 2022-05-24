# import heapq
# import sys
#
# N = int(input())
# a=[]
#
# for i in range(0,N):
#     b = int(sys.stdin.readline())
#     heapq.heappush(a, b)
#
# for j in range(0, len(a)):
#     print(heapq.heappop(a))
import heapq
import sys

n = int(input())
hp = []
for i in range(n):
    heapq.heappush(hp, int(sys.stdin.readline()))

for i in range(n):
    print(heapq.heappop(hp))
