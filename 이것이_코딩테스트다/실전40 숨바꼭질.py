import collections
import heapq

node, edge = map(int, input().split())

graph = [[] for _ in range(node+1)]
for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [1e9] * (node+1)
distance[1] = 0
qu = []
heapq.heappush(qu, (0, 1))
 #0이 거리, 1이 위치

while qu:
    dist, now = heapq.heappop(qu)

    if dist > distance[now]:
        continue

    for w in graph[now]:
        cost = dist + 1
        if cost < distance[w]:
            distance[w] = cost
            heapq.heappush(qu, (cost, w))

count = 0
result = 0
index = 0
for i in range(1, node+1):
    if distance[i] > result:
        result = distance[i]
        count = 1
        index = i
    elif distance[i] == result:
        count += 1

print(index, result, count)