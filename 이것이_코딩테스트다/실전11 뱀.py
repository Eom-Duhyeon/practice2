"""
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

답 9


10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L

답 13
"""


board_size = int(input())
board = [[0]*board_size for _ in range(board_size)]
apple = int(input())
for i in range(apple):
    a, b = map(int, input().split())
    board[a-1][b-1] = 2

order = {}
command = int(input())
for i in range(command):
    a, b = input().split()
    order[int(a)] = b

snake = [(0,0)]
board[0][0] = 1

direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

time = 0

while True:
    time += 1

    head = snake[-1]
    x, y = head[0], head[1]
    nx = x + dx[direction]
    ny = y + dy[direction]
    if nx < 0 or nx >= board_size or ny < 0 or ny >= board_size or board[nx][ny] == 1:
        print(time)
        exit()

    if board[nx][ny] == 2:
        board[nx][ny] = 1
        snake.append((nx, ny))
    else:
        board[nx][ny] = 1
        snake.append((nx, ny))
        r, t = snake.pop(0)
        board[r][t] = 0
    if time in order:
        if order[time] == "D":
            direction = (direction+1) % 4
        elif order[time] == "L":
            direction = (direction-1) % 4





print(order)
# print(board_size)
# print(n)
# for i in range(n):
#     print(apple[i])
# for i in range(m):
#     print(order[i])