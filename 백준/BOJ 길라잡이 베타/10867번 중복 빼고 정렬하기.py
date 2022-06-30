# import sys
# N = int(input())
#
# a = [int(x) for x in sys.stdin.readline().split()]
# a = set(a)
# print(*(sorted(a)))
import sys

cnt = [0]*(2001)
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
for i in nums:
    cnt[i+1000] += 1

for i in range(2001):
    if cnt[i]:
        print(i-1000, end=" ")