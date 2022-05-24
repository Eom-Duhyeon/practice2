import heapq

mat = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    heapq.heappush(mat, (y, x))

for i in range(n):
    y, x = heapq.heappop(mat)
    print(x, y, sep=" ")
