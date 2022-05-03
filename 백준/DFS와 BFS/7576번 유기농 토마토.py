# 토마토의 위치를 큐에 넣고 다음을 하나씩 꺼낸다. 처음 주어진 토마토는 1, 1때문에 익은 토마토는 2, 2때문에 익은 토마토는 3... 이런 식으로
# 날짜를 계산한다. 토마토가 없는 위치는 주변을 익히지 못하는 1 토마토와 다를 게 없다. 즉 0일 때만 bfs를 진행한다.
import collections

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while tomatoes:
        x, y = tomatoes.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                if ground[nx][ny] == 0:
                    ground[nx][ny] = ground[x][y] + 1
                    tomatoes.append((nx, ny))


m, n = map(int, input().split())
ground = []
tomatoes = collections.deque([])
ground =[list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if ground[i][j] == 1:
            tomatoes.append((i, j))

bfs()

for i in ground:
    if 0 in i:
        print(-1)
        exit()

print(max(max(ground))-1)

# from collections import deque
#
# m, n = map(int, input().split())
# ground = [list(map(int, input().split())) for _ in range(n)]
# tomatoes = deque([])
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# res = 0
#
# for i in range(n):
#     for j in range(m):
#         if ground[i][j] == 1:
#             tomatoes.append([i, j])
#
# def bfs():
#     while tomatoes:
#         x, y = tomatoes.popleft()
#         for u in range(4):
#             nx, ny = dx[u] + x, dy[u] + y
#             if 0 <= nx < n and 0 <= ny < m and ground[nx][ny] == 0:
#                 ground[nx][ny] = ground[x][y] + 1
#                 tomatoes.append([nx, ny])
#
# bfs()
# for i in ground:
#     for j in i:
#         if j == 0:
#             print(-1)
#             exit(0)
#     res = max(res, max(i))
# print(res - 1)
