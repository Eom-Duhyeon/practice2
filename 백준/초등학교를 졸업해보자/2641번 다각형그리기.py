import sys

#직접 그려서 비교해본다.
n = int(input())
arr = [int(x) for x in sys.stdin.readline().split()]
shape = [[0 for j in range(101)] for i in range(101)]
shape[50][50] = 1
dx = [0, 1, 0, -1, 0]
dy = [0, 0, 1, 0, -1]

x, y = 0,0
for i in arr:
    x += dx[i]
    y += dy[i]
    shape[50+x][50+y] = 1

num = int(input())
matrix = [[0 for j in range(n)] for i in range(num)]

xx, yy = 0,0
answer1 = 0
answer2 = []
for i in range(num):
    matrix[i] = [int(x) for x in sys.stdin.readline().split()]
    for j in matrix[i]:
        shape2 = [[0 for q in range(101)] for w in range(101)]
        shape2[50][50] = 1
        xx += dx[j]
        yy += dy[j]
        shape[50 + xx][50 + yy] = 1
        if shape == shape2:
            answer1 += 1
            answer2.append(matrix[i])

print(answer1)
for row in answer2:
    print(answer2[row])



