# import sys
#
# n = int(input())
#
# house = []
#
# for i in range(n):
#     house.append(list(int(x) for x in sys.stdin.readline().split()))
#
# for i in range(1, n):
#     house[i][0] += min(house[i - 1][1], house[i-1][2])
#     house[i][1] += min(house[i - 1][0], house[i - 1][2])
#     house[i][2] += min(house[i - 1][1], house[i - 1][0])
#
# print(min(house[n-1]))

"""
3
26 40 83
49 60 57
13 89 99

8
71 39 44
32 83 55
51 37 63
89 29 100
83 58 11
65 13 15
47 25 29
60 66 19

"""
import sys

n = int(sys.stdin.readline())
house = []
for i in range(n):
    house.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    house[i][0] += min(house[i - 1][1], house[i - 1][2])
    house[i][1] += min(house[i - 1][0], house[i - 1][2])
    house[i][2] += min(house[i - 1][0], house[i - 1][1])

print(min(house[n-1]))
