import collections
import sys

n, m, start = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]

for i in graph:
    graph[i].sort()

visited = []

def dfs(graph, start):
    visited.append(start)
    print(start, end=" ")
    for w in graph[start]:
        if w not in visited:
            dfs(graph, w)

visited_b = []

def bfs(graph, start):
    q= collections.deque()
    q.append(start)
    while q:
        v = q.popleft()
        visited_b.append(v)
        print(v, end= " ")
        for w in graph[v]:
            if w not in visited_b and w not in q:
                q.append(w)

dfs(graph, start)
print()
bfs(graph, start)
