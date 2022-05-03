# import collections
#
# node, line, distance, start = map(int, input().split())
# graph=[[] for _ in range(node+1)]
# for i in range(line):
#     a, b = map(int, input().split())
#     graph[a] += [b]
#
# visited = [False]*(node +1)
#
# qu = collections.deque()
# qu.append((start, 0))
#
# answer = []
#
# while qu:
#     now, dist = qu.pop()
#     if dist == distance:
#         answer.append(now)
#     for w in graph[now]:
#         if visited[w] == False:
#             visited[w] = True
#             qu.append((w, dist+1))
#
# if not answer:
#     print(-1)
# else:
#     answer.sort()
#     for ans in answer:
#         print(ans)
import collections

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1]*(n+1)

distance[x] = 0

qu = collections.deque([x])

while qu:
    now = qu.popleft()

    for w in graph[now]:
        if distance[w] == -1:
            distance[w] = distance[now] +1
            qu.append(w)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)


