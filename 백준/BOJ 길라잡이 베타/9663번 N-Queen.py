# i,j에 대해 j의 위치를 인덱스[i]의 값으로 두면 2차원 배열 안 써도 된다.

# 어차피 한 행에 하나씩 놓을 것이니 2가지만 검사하면 된다. 같은 열에 있는지, 대각선 상에 있는지-이것은 abs로 한 가지로 줄일 수 있다.
#promising을 하나로 합칠 수가 없다. range(0)에서 (n이 0일 때) 문제가 난다.

n = int(input())

answer = 0
row = [0] * n


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True


def n_queens(x):
    global answer
    if x == n:
        answer += 1
        return

    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)


n_queens(0)
print(answer)