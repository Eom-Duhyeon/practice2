import sys
import heapq
N = int(input())
l=[]
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(l,(b,a))
for j in range(N):
    c=heapq.heappop(l)
    print(c[1], c[0])
