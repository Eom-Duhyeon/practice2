"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

"""
import itertools

def dfs(x, y):
    if x<0 or x>= n or y <0 or y>= m or lab[x][y] != 0:
        return

    lab[x][y] = 3
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)



n, m = map(int, input().split())

lab_origin = []

for i in range(n):
    lab_origin.append(list(map(int, input().split())))

lab = [i[:] for i in lab_origin]

wall_candidate = []

for i in range(n):
    for j in range(m):
        wall_candidate.append((i, j))




answer = 0
for wall in itertools.combinations(wall_candidate, 3):
    if lab[wall[0][0]][wall[0][1]] != 0 or lab[wall[1][0]][wall[1][1]] != 0 or lab[wall[2][0]][wall[2][1]] != 0:
        continue

    lab[wall[0][0]][wall[0][1]] = 1
    lab[wall[1][0]][wall[1][1]] = 1
    lab[wall[2][0]][wall[2][1]] = 1

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                lab[i][j] = 0
                dfs(i, j)

    cnt = 0
    for i in range(n):
        cnt += lab[i].count(0)

    answer = max(answer, cnt)
    lab = [i[:] for i in lab_origin]

print(answer)
여기까지가 나의 제출 정답이었다

# n, m = map(int, input().split())
# data = []
# temp = [[0] * m for _ in range(n)]
#
# for _ in range(n):
#     data.append(list(map(int, input().split())))
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# result = 0
#
# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if nx >= 0 and nx < n and ny >=0 and ny <m:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = 2
#                 virus(nx, ny)
#
# def get_score():
#     score = 0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 score += 1
#
#     return score
#
# def dfs(count):
#     global result
#
#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = data[i][j]
#
#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(i, j)
#
#         result = max(result, get_score())
#         return
#
#     for i in range(n):
#         for j in range(m):
#             if data[i][j] == 0:
#                 data[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 data[i][j] = 0
#                 count -= 1
#
# dfs(0)
# print(result)
#
# # 월등히 성능이 나쁘다




