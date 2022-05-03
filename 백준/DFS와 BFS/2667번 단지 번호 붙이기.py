"""
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

예제 입력 1
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
예제 출력 1
3
7
8
9
"""
import sys

n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, sys.stdin.readline().rstrip()))) #띄어쓰기가 없는 격자 rstrip으로 받자

house = 0

def dfs(i, j):
    if i < 0 or j < 0 or i > (n-1) or j > (n-1) or grid[i][j] != 1:
        return
    grid[i][j] = 0
    global house
    house += 1
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)

count = 0
result = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            dfs(i,j)
            count+=1
            result.append(house)
            house = 0

result.sort()
print(count)
for _ in result:
    print(_)