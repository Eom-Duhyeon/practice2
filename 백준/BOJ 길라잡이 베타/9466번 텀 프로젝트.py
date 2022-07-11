

import sys
sys.setrecursionlimit(100000)

def dfs(i):
    global result
    visited[i] = True
    cycle.append(i)
    team = teams[i]
    if visited[team]:
        if team in cycle:
            result += cycle[cycle.index(team):]
        pass
    else:
        dfs(team)


for _ in range(int(input())):
    length = int(input())
    teams = [0] + list(map(int, input().split()))
    visited = [True] + [False]*length
    result = []

    for i in range(1, length+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(length - len(result))

"""
2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8

출력
3
0
"""

