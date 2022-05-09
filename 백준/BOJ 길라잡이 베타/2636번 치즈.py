import collections

n, m = map(int, input().split())


table = []
for i in range(n):
    table.append(list(map(int, input().split())))


day = 0

cheeses = [0, 0]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs():
    visited = [[False]*m for _ in range(n)]
    qu = collections.deque()
    qu.append((0,0))
    global count
    visited[0][0] = True
    while qu:
        x, y = qu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] == True:
                continue

            if table[nx][ny] == 1:
                visited[nx][ny] = True
                count += 1
                table[nx][ny] = 0
            elif table[nx][ny] == 0:
                visited[nx][ny] = True
                qu.append((nx, ny))




while True:
    count = 0
    dfs()
    day += 1
    cheeses.append(count)
    if count == 0:
        break




print(day-1)
print(cheeses[-2])


"""
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0

"""