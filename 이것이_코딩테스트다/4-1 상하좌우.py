"""
입력 예시
5
R R R U D D
출력 예시
3 4
"""

N = int(input())
orders = list(input().split())

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

direction = {"L":0, "R":1, "U":2, "D":3}

for order in orders:
    nx = x + dx[direction[order]]
    ny = y + dy[direction[order]]
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    x = nx
    y = ny

print(x, y)