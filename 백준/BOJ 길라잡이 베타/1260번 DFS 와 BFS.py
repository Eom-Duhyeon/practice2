# import collections
# import sys
#
# n, m, start = map(int, sys.stdin.readline().split())
# graph = collections.defaultdict(list)
# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a] += [b]
#     graph[b] += [a]
#
# for i in graph:
#     graph[i].sort()
#
# visited = []
#
# def dfs(graph, start):
#     visited.append(start)
#     print(start, end=" ")
#     for w in graph[start]:
#         if w not in visited:
#             dfs(graph, w)
#
# visited_b = []
#
# def bfs(graph, start):
#     q= collections.deque()
#     q.append(start)
#     while q:
#         v = q.popleft()
#         visited_b.append(v)
#         print(v, end= " ")
#         for w in graph[v]:
#             if w not in visited_b and w not in q:
#                 q.append(w)
#
# dfs(graph, start)
# print()
# bfs(graph, start)

#DFS 먼저, BFS 나중에
import collections

n, m, v = map(int, input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

for i in range(1, n+1):
    graph[i].sort()

dfs_path=[]

def dfs(v):
    if len(dfs_path) == n:
        return
    dfs_path.append(v)
    for w in graph[v]:
        if w not in dfs_path:
            dfs(w)

#### 매우 중요 : w가 path에서도 물론 없어야 하지만 qu에도 없어야 한다는 것을 명심. qu에 있는데 반환해버리면 더 이상 bfs가 아니다.
bfs_path=[]
def bfs(v):
    qu = collections.deque()
    qu.append(v)

    while qu:
        now = qu.popleft()
        bfs_path.append(now)
        if len(bfs_path) == n:
            return
        for w in graph[now]:
            if w not in bfs_path and w not in qu:
                qu.append(w)

dfs(v)
bfs(v)

for i in dfs_path:
    print(i, end=" ")

print()

for i in bfs_path:
    print(i, end=" ")
