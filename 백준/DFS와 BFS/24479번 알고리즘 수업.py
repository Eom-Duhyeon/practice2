n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort(reverse=True)

visited = [True] + [False]*n
stack = [start]
answer = [0]*(n+1)
idx = 0


visited[start] = True


while stack:
    now = stack.pop()
    idx += 1
    answer[now] = idx
    for w in graph[now]:
        if not visited[w]:
            visited[w] = True
            stack.append(w)

for i in range(1, n+1):
    print(answer[i])



