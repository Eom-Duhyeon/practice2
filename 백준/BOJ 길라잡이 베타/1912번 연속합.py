import sys

n = int(input())
numbers = list(int(x) for x in sys.stdin.readline().split())

buff = 0
maxi = numbers[0]
for i in range(n):
    buff += numbers[i]
    if buff > maxi:
        maxi = buff
    if buff < 0:
        buff = 0

print(maxi)
"""
10
10 -4 3 1 5 6 -35 12 21 -1

10
2 1 -4 3 4 -4 6 5 -5 1

5
-1 -2 -3 -4 -5

"""
