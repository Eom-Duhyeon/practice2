

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
n = len(key)
m = len(lock)

door = [[0] * (3*m) for _ in range(3*m)]
for i in range(m, 2 * m):
    for j in range(m, 2 * m):
        door[i][j] = lock[i - m][j - m]
def turn(key):
    l = len(key)
    buff = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            buff[j][l - i - 1] = key[i][j]
    return buff

key = turn(key)

def check(door):
    t = len(door) // 3
    for i in range(t, 2 * t):
        for j in range(t, 2 * t):
            if door[i][j] != 1:
                return False
    return True

for a in range(n):
    for b in range(n):
        door[4+a][4+b] += key[a][b]

print(check(door))


