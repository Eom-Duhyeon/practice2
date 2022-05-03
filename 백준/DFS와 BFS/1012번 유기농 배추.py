"""
입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

예제 입력 1
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
예제 출력 1
5
1
"""
import sys

def dfs(i,j):
    if i < 0 or j < 0 or i > n-1 or j > m-1 or grid[i][j] == 0:
        return
    grid[i][j] = 0
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)


repeat = int(input())
show = []
for _ in range(repeat):
    n, m, k = map(int, sys.stdin.readline().split()) # 가로 세로 배추의 개수
    grid=[[0]*m for i in range(n)] # 가로n, 세로 m 격자 만들기
    count = 0
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        grid[x][y] = 1


    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dfs(i, j)
                count += 1

    show.append(count)

for j in show:
    print(j)

