# import heapq
#
# n = int(input()) # 주유소 개수
# station = []
# for i in range(n):
#     dist, f = map(int, input().split())
#     heapq.heappush(station, (dist, f))
# distance, fuel = map(int, input().split())
# possible = []
# count = 0
#
# while fuel < distance:
#
#     while station and fuel >= station[0][0]:
#         dist, f = heapq.heappop(station)
#         heapq.heappush(possible, -f)
#
#     if possible:
#         fuel -= heapq.heappop(possible)
#         count += 1
#     elif not station or fuel < station[0][0]:
#         break
#
# if fuel >= distance:
#     print(count)
# else:
#     print(-1)

"""
4
4 4
5 2
11 5
15 10
25 10
"""

# max힙 possible이 하나 더 필요하다. 연료로 갈 수 있는 곳 까지를 전부 possible에 담는다. 힙에서 하나 뽑을 때마다 갈 수 있는 모든 거리를 possible에 넣는다.
import heapq
import sys

n = int(sys.stdin.readline())
station = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split()) # a는 위치 b는 연료
    heapq.heappush(station, (a, b))
l, p = map(int, sys.stdin.readline().split()) # l은 거리, p는 원래 있었던

possible = []
cnt = 0
while p < l:

    while station and station[0][0] <= p:
        dist, fuel = heapq.heappop(station)
        heapq.heappush(possible, -fuel)

    if possible:
        p -= heapq.heappop(possible)
        cnt += 1

    elif not station or station[0][0] > p:
        break

if p >= l:
    print(cnt)
else:
    print(-1)
