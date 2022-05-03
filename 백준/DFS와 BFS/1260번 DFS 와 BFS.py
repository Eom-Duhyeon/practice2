"""
정답코드
"""
import collections
import sys


def dfs(n):
    print(n, end="")
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

def bfs(n):
    visited[n] = True
    qu = collections.deque([n])
    while qu:
        v = qu.popleft()
        print(v, end="")
        for w in graph[v]:
            if not visited[i]:
                qu.append(w)
                visited[w] = True


n, m, v = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfs(v)
visited = [False] * (n+1)
print()
bfs(v)