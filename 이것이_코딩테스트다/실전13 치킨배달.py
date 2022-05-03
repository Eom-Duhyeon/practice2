"""
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

답 5

5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

답 10


"""
import itertools

length, remain = map(int, input().split())

city = []

for i in range(length):
    city.append(list(map(int, input().split())))


house = []
chicken = []
for i in range(length):
    for j in range(length):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

def chick_meter (a, b, c, d):
    return abs(a - c) + abs(b - d)



answer = 1e9
for ch in itertools.combinations(chicken, remain):
    summary = 0
    for home in house:
        chicken_meter = 10000000000
        for i in ch:
            chicken_meter = min(chicken_meter, chick_meter(i[0], i[1], home[0], home[1]))

        summary += chicken_meter

    answer = min(answer, summary)

print(answer)

