# import sys
#
# n = int(input()) # 도시 개수
# length = [int(x) for x in input().split()]
# price = [int(y) for y in input().split()]
#
# city = []
# for i in range(n-1):
#     city.append((price[i], length[i]))
#
#
#
# sum = 0
#
# stop=city[0][0]
# road=city[0][1]
# if n == 2:
#     sum = stop*road
# else:
#     for i in range(1, n - 1):
#         if stop > city[i][0]:
#             sum += stop * road
#             stop = city[i][0]
#             road = city[i][1]
#         else:
#             road += city[i][1]
#     sum += road * stop
#
# print(sum)

"""
4
2 3 1
5 2 4 1
출력 : 18

4
3 3 4
1 1 1 1
출력 : 10

"""

#길이, 가격 순

# 두 번째 도시까지 갈 때는 무조건 첫 번째 도시에서 주유를 해야 한다. 만약 도착한 도시의 기름값이 더 싸면 그 때 주유소를 갱신한다
# 아니라면 주유소를 갱신할 필요 없이 (첫 번째 주유소*두 번째에서 세 번째 가는 길)을 총 합으로 더하면 된다.
# 아래 코드가 더 간결하다

import sys

n = int(sys.stdin.readline())
loads = list(map(int, sys.stdin.readline().split()))
costs = list(map(int, sys.stdin.readline().split()))

station = costs[0]
answer = station*loads[0]
if n == 2:
    print(answer)
    exit()

for i in range(1, n-1):
    if costs[i] < station:
        station = costs[i]
    answer += station*loads[i]
print(answer)
