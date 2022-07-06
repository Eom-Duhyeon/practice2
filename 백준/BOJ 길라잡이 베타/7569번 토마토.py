
# import collections
#
# a, b, c = map(int, input().split())
# box = [[] for _ in range(c)]
# for k in range(c):
#     for i in range(b):
#         box[k].append(list(map(int, input().split())))
#
# tomatoes = collections.deque()
# for i in range(c):
#     for j in range(b):
#         for k in range(a):
#             if box[i][j][k] == 1:
#                 tomatoes.append((i, j, k, 1))
#
# dx = [0, 0, 0, 0, 1, -1]
# dy = [0, 0, 1, -1, 0, 0]
# dz = [1, -1, 0, 0, 0, 0]
#
#
#
# while tomatoes:
#     x, y, z, day = tomatoes.popleft()
#     for i in range(6):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         nz = z + dz[i]
#         if nx < 0 or nx >= c or ny < 0 or ny >= b or nz < 0 or nz >= a:
#             continue
#         if box[nx][ny][nz] == 0:
#             box[nx][ny][nz] = day + 1
#             tomatoes.append((nx, ny, nz, day + 1))
#
# maximum = 0
# flag = False
# for i in range(c):
#     for j in range(b):
#         for k in range(a):
#             if box[i][j][k] == 0:
#                 flag = True
#                 break
#             else:
#                 if box[i][j][k] > maximum:
#                     maximum = box[i][j][k]
#
# if flag == True:
#     print(-1)
# else:
#     print(maximum - 1)

"""
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
"""
import collections
import sys

a, b, c = map(int, sys.stdin.readline().split())
box = [[] for _ in range(c)]
tomatoes = collections.deque()

for i in range(c):
    for j in range(b):
        box[i].append(list(map(int, sys.stdin.readline().split())))

for i in range(c):
    for j in range(b):
        for k in range(a):
            if box[i][j][k] == 1:
                tomatoes.append((i, j, k, 1))

dx =[0, 0, 0, 0, 1, -1]
dy =[0, 0, 1, -1, 0, 0]
dz =[1, -1, 0, 0, 0, 0]


while tomatoes:
    z, y, x, day = tomatoes.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nz < 0 or nz >= c or ny < 0 or ny >= b or nx < 0 or nx >= a:
            continue
        if box[nz][ny][nx] == 0:
            box[nz][ny][nx] = day + 1
            tomatoes.append((nz, ny, nx, day + 1))

max_day = 0

for i in range(c):
    for j in range(b):
        for k in range(a):
            if box[i][j][k] == 0:
                print(-1)
                exit()
            if box[i][j][k] > max_day:
                max_day = box[i][j][k]

print(max_day-1)
