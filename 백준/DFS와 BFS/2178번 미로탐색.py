"""
입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제 입력 1
4 6
101111
101010
101011
111011
예제 출력 1
15

예제 입력 3
2 25
1011101110111011101110111
1110111011101110111011101
예제 출력 3
38
"""
import collections
import sys

n, m = map(int, input().split())

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    qu = collections.deque()
    qu.append((0, 0))
    while qu:
        x, y = qu.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if nx < 0 or ny < 0 or nx > (n-1) or ny > (m-1) or grid[nx][ny] == 0:
                continue
            if grid[nx][ny] == 1:
                grid[nx][ny] = grid[x][y] + 1
                qu.append((nx, ny))
    return grid[n-1][m-1]


grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().rstrip())))

print(bfs())