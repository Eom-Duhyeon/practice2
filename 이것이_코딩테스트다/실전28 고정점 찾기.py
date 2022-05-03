"""
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
"""

length = int(input())
data = list(map(int, input().split()))

start = 0
end = length - 1

while start <= end:
    mid = (start+end)//2
    if data[mid] == mid:
        break

    if data[mid] < mid:
        start = mid + 1
    elif data[mid] > mid:
        end = mid -1

if start > end:
    print(-1)
else:
    print(mid)