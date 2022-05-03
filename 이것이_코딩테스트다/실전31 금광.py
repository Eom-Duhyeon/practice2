testcases = int(input())
for testcase in range(testcases):
    n, m = map(int, input().split())
    mine = [[0]*m for _ in range(n)]
    data = list(map(int, input().split()))
    for i in range(n*m):
        mine[i//m][i % m] = data[i]

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                mine[i][j] += max(mine[0][j-1], mine[1][j-1])
            elif i == n-1:
                mine[i][j] += max(mine[n-2][j-1], mine[n-1][j-1])
            else:
                mine[i][j] += max((mine[i-1][j-1], mine[i][j-1], mine[i+1][j-1]))

    answer = mine[0][m-1]
    for i in range(1,n):
        if answer < mine[i][m-1]:
            answer = mine[i][m-1]

    print(answer)


