import collections
import heapq
import sys

v, e = map(int, input().split())
start = int(input())
graph = [[]for i in range(v+1)]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))


INF = 1e9
distance = [INF]*(v+1)

qu = []
heapq.heappush(qu, (0, start))
distance[start] = 0

while qu:
    dist, now = heapq.heappop(qu)
    if dist > distance[now]:
        continue
    else:
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(qu, (cost, i[0]))

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

"""