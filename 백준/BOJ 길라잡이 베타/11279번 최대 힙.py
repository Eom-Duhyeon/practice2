# import heapq
# import sys
#
# n = int(input())
#
# hea = []
# for i in range(n):
#     a = int(sys.stdin.readline())
#     a = -a
#     if a == 0:
#         if hea:
#             print((-1)*heapq.heappop(hea))
#         else:
#             print(0)
#     else:
#         heapq.heappush(hea, a)

"""
13
0
1
2
0
0
3
2
1
0
0
0
0
0
"""
import heapq
import sys

hp =[]

for i in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a == 0:
        try:
            print(heapq.heappop(hp)[1])
        except:
            print(0)
    else:
        heapq.heappush(hp, (-a, a))