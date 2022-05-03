import sys

mat = [[0 for _ in range(101)] for _ in range(101)]

for i in range(0,4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for j in range(x1, x2):
        for k in range(y1, y2):
            mat[j][k] = 1

answer = 0

for row in mat:
    answer += sum(row)

print(answer)

