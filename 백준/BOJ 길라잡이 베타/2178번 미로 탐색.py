import collections
import sys

n, m = map(int, sys.stdin.readline().split())

maze = []
for i in range(n):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))

qu = collections.deque()
qu.append((0, 0, 1))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while qu:
    x, y, cost = qu.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if maze[nx][ny] == 1:
            maze[nx][ny] = cost + 1
            qu.append((nx, ny, cost + 1))

print(maze[n - 1][m - 1])
"""
4 6
101111
101010
101011
111011

출력 : 15

4 6
110110
110110
111111
111101
출력 : 9
"""