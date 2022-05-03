def turn(key):
    l = len(key)
    buff = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            buff[j][l - i - 1] = key[i][j]
    return buff