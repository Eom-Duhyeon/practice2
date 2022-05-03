"""
입력
4 5
00110
00011
11111
00000

출력
3
"""

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(x,y):
    if x<0 or x >= N or y <0 or y>= M or graph[x][y] == 1:
        return

    graph[x][y] = 1
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)

result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            dfs(i,j)
            result += 1

print(result)