

# import sys
#
# n = int(input())
# grid = []
# for i in range(n):
#     grid.append(list(map(int, sys.stdin.readline().rstrip()))) #띄어쓰기가 없는 격자 rstrip으로 받자
#
# house = 0
#
# def dfs(i, j):
#     if i < 0 or j < 0 or i > (n-1) or j > (n-1) or grid[i][j] != 1:
#         return
#     grid[i][j] = 0
#     global house
#     house += 1
#     dfs(i+1, j)
#     dfs(i-1, j)
#     dfs(i, j+1)
#     dfs(i, j-1)
#
# count = 0
# result = []
# for i in range(n):
#     for j in range(n):
#         if grid[i][j] == 1:
#             dfs(i,j)
#             count+=1
#             result.append(house)
#             house = 0
#
# result.sort()
# print(count)
# for _ in result:
#     print(_)

"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
import sys
n = int(sys.stdin.readline())
grid = []
for i in range(n):
    grid.append(list(map(int, sys.stdin.readline().rstrip())))

house = 0

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] == 0:
        return

    grid[x][y] = 0
    global house
    house += 1
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)

answer = []
cnt = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            dfs(i, j)
            cnt += 1
            answer.append(house)
            house = 0

answer.sort()
print(cnt)
for i in answer:
    print(i)