# a = [1, 2, 3, 4]
# b = [2, 3]
# c = [x for x in a if x not in b]
# print(c)
# import itertools
# import sys
#
# n = int(input())
# data = []
# for i in range(n):
#     data.append(list(int(x) for x in sys.stdin.readline().split()))
#
# l = [x for x in range(n)]
#
# diff = 1e9
# for start in list(itertools.combinations(l, n//2)):
#     link = [x for x in l if x not in start]
#     start_score = 0
#     link_score = 0
#     for fair in list(itertools.combinations(start, 2)):
#         start_score += (data[fair[1]][fair[0]] + data[fair[0]][fair[1]])
#     for fair in list(itertools.combinations(link, 2)):
#         link_score += (data[fair[1]][fair[0]] + data[fair[0]][fair[1]])
#     diff = min(diff, abs(start_score - link_score))
#
# print(diff)
"""
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0
"""
import itertools
import sys

n = int(input())

team = []
for i in range(n):
    team.append(list(map(int, sys.stdin.readline().split())))

min_diff = 1e9
for start in itertools.combinations([int(x) for x in range(n)], n//2):
    link = [int(x) for x in range(n) if x not in start]
    sum_link = 0
    sum_start = 0
    for two in itertools.combinations(start, 2):
        sum_start += team[two[0]][two[1]] + team[two[1]][two[0]]

    for two in itertools.combinations(link, 2):
        sum_link += team[two[0]][two[1]] + team[two[1]][two[0]]

    if abs(sum_start - sum_link) < min_diff:
        min_diff = abs(sum_start - sum_link)

print(min_diff)
