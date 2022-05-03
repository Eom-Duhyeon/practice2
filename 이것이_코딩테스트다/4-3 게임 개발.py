"""
0이 육지, 1이 바다
입력 예시
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
출력예시
3

"""

N, M = map(int, input().split())
x, y, direction = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

#방향 : 북 동 남 서. 회전은 왼쪽부터니까 -1씩
dx = [-1, 0 ,1, 0]
dy = [0, -1, 0, 1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if graph[nx][ny] == 0:
        graph[nx][ny] = 1
        x, y = nx, ny
        count += 1
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        break
    turn_time = 0

print(count)
