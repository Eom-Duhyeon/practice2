import collections

for tc in range(int(input())):
    n = int(input())
    indegree = [0] * (n+1)
    graph = [[False] * (n+1) for i in range(n+1)]
    data = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1


    result = []
    q = collections.deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True # 위상 정렬 결과가 오직 하나인지의 여부
    cycle = False # 사이클이 존재하는지 확인

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break # 큐가 빈다면 사이클이 발생했다는 뜻

        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)

        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1

                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print(("IMPOSSIBLE"))
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()