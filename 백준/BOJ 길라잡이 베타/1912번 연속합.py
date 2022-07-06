# import sys
#
# n = int(input())
# numbers = list(int(x) for x in sys.stdin.readline().split())
#
# buff = 0
# maxi = numbers[0]
# for i in range(n):
#     buff += numbers[i]
#     if buff > maxi:
#         maxi = buff
#     if buff < 0:
#         buff = 0
#
# print(maxi)

"""
10
10 -4 3 1 5 6 -35 12 21 -1

10
2 1 -4 3 4 -4 6 5 -5 1

5
-1 -2 -3 -4 -5
"""
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
if n == 1:
    print(num[0])
    exit()

sum_v = 0
max_v = num[0]
for i in range(n):
    sum_v += num[i]
    max_v = max(max_v, sum_v)
    if sum_v < 0:
        sum_v = 0

print(max_v)