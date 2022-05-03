import sys

n, target = map(int, input().split())
trees = [int(x) for x in sys.stdin.readline().split()]
trees.sort()

start = 1
end = trees[-1]

while start <= end:
    num = 0
    mid = (start+end)//2
    for tree in trees:
        if tree > mid:
            num += tree - mid
    if num >= target:
        start = mid + 1
    else:
        end = mid - 1

print(end)





"""

4 7
20 15 10 17

5 20
4 42 40 26 46
"""