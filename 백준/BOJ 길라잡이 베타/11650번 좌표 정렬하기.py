# import sys
# import heapq
# N = int(input())
# l=[]
# for i in range(N):
#     a, b = map(int, sys.stdin.readline().split())
#     heapq.heappush(l,(b,a))
# for j in range(N):
#     c=heapq.heappop(l)
#     print(c[1], c[0])
import heapq
import sys

hp = []
n = int(input())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(hp, (a, b))

for i in range(n):
    a, b = heapq.heappop(hp)
    print(a, b)
