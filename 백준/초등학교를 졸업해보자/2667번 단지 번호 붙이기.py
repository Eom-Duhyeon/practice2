from sys import stdin
n = int(input())

# 데이터 저장용 공간 matrix
matrix = [[0]*n for _ in range(n)]
# 방문 내역 저장용 visited
visited = [[0]*n for _ in range(n)]

for i in range(n):
    line = stdin.readline().strip()
    for j, b in enumerate(line):
        matrix[i][j] = int(b)

# 방향 확인용 좌표 dx와 dy
# 중앙을 기준으로 좌/우/위/아래
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]