# import sys
#
# n = int(input())
# data = list(map(int, sys.stdin.readline().split()))
# data.sort()
# print(data[0]*data[-1])

"""

1
2

6
3 4 2 12 6 8

14
14 26456 2 28 13228 3307 7 23149 8 6614 46298 56 4 92596
"""
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
print(max(nums)*min(nums))