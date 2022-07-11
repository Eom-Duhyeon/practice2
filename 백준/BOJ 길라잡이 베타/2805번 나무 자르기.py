# import sys
#
# n, target = map(int, input().split())
# trees = [int(x) for x in sys.stdin.readline().split()]
# trees.sort()
#
# start = 1
# end = trees[-1]
#
# while start <= end:
#     num = 0
#     mid = (start+end)//2
#     for tree in trees:
#         if tree > mid:
#             num += tree - mid
#     if num >= target:
#         start = mid + 1
#     else:
#         end = mid - 1
#
# print(end)

"""

4 7
20 15 10 17

5 20
4 42 40 26 46
"""
import sys

n, m = map(int, sys.stdin.readline().split()) # n은 나무 갯수 , m은 가져가고 싶은 길이

trees = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(trees)

while start <= end:
    mid = (start+end)//2
    sum_t = 0
    for tree in trees:
        if tree > mid:
            sum_t += (tree - mid)
    if sum_t < m:
        end = mid-1
    else:
        start = mid + 1

print(end)