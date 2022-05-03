node = int(input())
edge = int(input())
graph = [[1e9]*node for _ in range(node)]

for i in range(edge):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for i in range(node):
    graph[i][i] = 0

for k in range(node):
    for i in range(node):
        for j in range(node):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(node):
    for j in range(node):
        if graph[i][j] == 1e9:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()