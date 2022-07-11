import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
v = int(input())
parent = [i for i in range(n + 1)]

for _ in range(v):
    a, b = map(int, input().split())
    union(parent, a, b)

print(parent)

answer = 0

# 위의 for문이 끝나도 최종적으로 다시 한 번 돌아 find하지 않으면 원하는 parent가 나오지 않는다.
# ex) [0, 1, 1, 1, 1, 5, 5, 1, 7, 7, 10] 이 때 검사 시에 find을 하는 것이 더 합리적이다.
# 7, 7인 elements들이 find에서 1을 반환할 것이다.
for i in range(1, n+1):
    if find(parent, i) == 1:
        answer += 1

print(answer-1)



"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""

# n = int(input())
# m = int(input())
#
# graph = [[] for _ in range(n+1)]
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# infected = 0
# visited = [False]*(n+1)
#
# def dfs(graph, v):
#     global infected
#     visited[v] = True
#     infected += 1
#     for w in graph[v]:
#         if not visited[w]:
#             dfs(graph, w)
#
# dfs(graph, 1)
# print(infected-1)


