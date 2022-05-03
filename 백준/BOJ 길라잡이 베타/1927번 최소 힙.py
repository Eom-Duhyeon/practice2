import heapq
import sys

hea = []
n = int(input())
for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if not hea:
            print(0)
        else:
            print(heapq.heappop(hea))
    else:
        heapq.heappush(hea, a)

"""
9
0
12345678
1
2
0
0
0
0
32
"""