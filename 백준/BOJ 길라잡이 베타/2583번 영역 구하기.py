# import collections
# import sys
# sys.setrecursionlimit(10 ** 6)
#
# n, m, k = map(int, input().split())
# data = [[0 for _ in range(m)] for p in range(n)]
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# for i in range(k):
#     a, b, c, d = map(int, input().split())
#     for i in range(b, d):
#         for j in range(a, c):
#             data[i][j] = 1
#
# answer = []
# qu = collections.deque()
# for i in range(n):
#     for j in range(m):
#         if data[i][j] == 0:
#             size = 0
#             qu.append((i, j))
#             while qu:
#                 x, y = qu.popleft()
#                 if 0<= x < n and 0 <= y < m:
#                     if data[x][y] == 0:
#                         data[x][y] = 1
#                         size += 1
#                         for i in range(4):
#                             nx = x + dx[i]
#                             ny = y + dy[i]
#                             qu.append((nx, ny))
#
#             answer.append(size)
# answer.sort()
# print(len(answer))
# for i in answer:
#     print(i, end=" ")


# import sys
#
# m, n, k = map(int, input().split())
# s = [[0] * n for i in range(m)]
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# cnt = []
# for i in range(k):
#     x1, y1, x2, y2 = map(int, input().split())
#     for j in range(y1, y2):
#         for k in range(x1, x2):
#             s[j][k] = 1
# for i in range(m):
#     for j in range(n):
#         if s[i][j] == 0:
#             count = 1
#             s[i][j] = 1
#             queue = [[i, j]]
#             while queue:
#                 x, y = queue[0][0], queue[0][1]
#                 del queue[0]
#                 for k in range(4):
#                     x1 = x + dx[k]
#                     y1 = y + dy[k]
#                     if 0 <= x1 < m and 0 <= y1 < n and s[x1][y1] == 0:
#                         s[x1][y1] = 1
#                         count += 1
#                         queue.append([x1, y1])
#             cnt.append(count)
# print(len(cnt))
# cnt.sort()
# for i in cnt:
#     print(i, end=' ')


"""
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
"""
import sys
sys.setrecursionlimit(10 ** 6)

m, n, k = map(int, sys.stdin.readline().split())
grid = [[0]*n for i in range(m)]

for i in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[y][x] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

size = 0
answer = []

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 1:
        return
    if grid[x][y] == 0:
        grid[x][y] = 1
        global size
        size += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            dfs(nx, ny)

for i in range(m):
    for j in range(n):
        if grid[i][j] == 0:
            dfs(i, j)
            answer.append(size)
            size = 0

answer.sort()
print(len(answer))
for a in answer:
    print(a, end=" ")
