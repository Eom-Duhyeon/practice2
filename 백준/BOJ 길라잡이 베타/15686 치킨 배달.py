# import itertools
# import sys
#
# size, remain = map(int, input().split())
# city = []
# chicken = []
# house = []
#
#
# for i in range(size):
#     city.append(list(int(x) for x in sys.stdin.readline().split()))
#
# for i in range(size):
#     for j in range(size):
#         if city[i][j] == 2:
#             chicken.append((i, j))
#         elif city[i][j] == 1:
#             house.append((i, j))
#
# answer = 1e9
#
# for ch in itertools.combinations(chicken, remain):
#     sumi = 0
#     for home in house:
#         ch_m = 1e9
#         for i in ch:
#             ch_m = min(abs(home[0]-i[0])+abs(home[1]-i[1]), ch_m)
#         sumi += ch_m
#     if sumi < answer:
#         answer = sumi
# print(answer)

"""
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0

5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
"""
import itertools
import sys

n, m = map(int, sys.stdin.readline().split())

city = []
for i in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))



def get_meter(x_1, y_1, x_2, y_2):
    return abs(x_1 - x_2) + abs(y_1 - y_2)

answer = 1e9
for remain in itertools.combinations(chicken, m):
    sum_meter = 0
    for home in house:
        meter = 1e9
        for i in remain:
            if get_meter(i[0], i[1], home[0], home[1]) < meter:
                meter = get_meter(i[0], i[1], home[0], home[1])
        sum_meter += meter

    if sum_meter < answer:
        answer = sum_meter

print(answer)
