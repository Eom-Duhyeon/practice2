"""
https://programmers.co.kr/learn/courses/30/lessons/60059
# ret = [[0] * N for _ in range(N)]
"""

"""
key	lock	result
[[0, 0, 0], [1, 0, 0], [0, 1, 1]]	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]	true

"""

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]





def solution(key, lock):

    key_length = len(key)
    lock_length = len(lock)

    #lock
    door_length = 2*(key_length-1) + lock_length
    door = [[0]*door_length for _ in range(door_length)]
    for i in range(lock_length):
        for j in range(lock_length):
            door[i+key_length-1][j+key_length-1] += lock[i][j]

    def turn(key):
        n = len(key)

        turned = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                turned[j][n - i - 1] = key[i][j]

        return turned

    def check(i, j):
        answer = True
        for a in range(key_length):
            for b in range(key_length):
                door[i+a][j+b] += key[a][b]

        for x in range(key_length-1, key_length + lock_length -1):
            for y in range(key_length - 1, key_length + lock_length - 1):
                if door[x][y] != 1:
                    answer = False
                    break

        for a in range(key_length):
            for b in range(key_length):
                door[i + a][j + b] -= key[a][b]

        return answer

    for _ in range(4):
        key = turn(key)
        for i in range(door_length-key_length+1):
            for j in range(door_length-key_length+1):
                if check(i, j):
                    return True


    return False

print(solution(key, lock))