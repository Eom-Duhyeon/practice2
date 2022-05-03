import collections

testcases = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for testcase in range(testcases):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    distance = [[1e9] * n for _ in range(n)]

    #다익스트라
    distance[0][0] = graph[0][0]
    qu = collections.deque()
    qu.append((0, 0, distance[0][0]))

    while qu:
        x, y, dist = qu.popleft()
        if dist > distance[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            cost = dist + graph[nx][ny]

            if distance[nx][ny] > cost:
                distance[nx][ny] = cost
                qu.append((nx, ny, cost))

    print(distance[n-1][n-1])