import heapq

n = int(input()) # 주유소 개수
station = []
for i in range(n):
    dist, f = map(int, input().split())
    heapq.heappush(station, (dist, f))
distance, fuel = map(int, input().split())
possible = []
count = 0

while fuel < distance:

    while station and fuel >= station[0][0]:
        dist, f = heapq.heappop(station)
        heapq.heappush(possible, -f)

    if possible:
        fuel -= heapq.heappop(possible)
        count += 1
    elif not station or fuel < station[0][0]:
        break

if fuel >= distance:
    print(count)
else:
    print(-1)
