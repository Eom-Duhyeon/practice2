import sys

n = int(input()) # 도시 개수
length = [int(x) for x in input().split()]
price = [int(y) for y in input().split()]

city = []
for i in range(n-1):
    city.append((price[i], length[i]))



sum = 0

stop=city[0][0]
road=city[0][1]
if n == 2:
    sum = stop*road
else:
    for i in range(1, n - 1):
        if stop > city[i][0]:
            sum += stop * road
            stop = city[i][0]
            road = city[i][1]
        else:
            road += city[i][1]
    sum += road * stop

print(sum)



