sudoku = [list(map(int, input().split())) for _ in range(9)]
# 꼭 기억해놓자. 깔끔하다
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def is_promising(i,j):
    promising = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #행렬 검사
    for x in range(9):
        if sudoku[x][j] in promising:
            promising.remove(sudoku[x][j])
        if sudoku[i][x] in promising:
            promising.remove(sudoku[i][x])

    #네모칸 검사
    a,b = i//3, j//3

    for x in range(3*a, 3*a+3):
        for y in range(3*b, 3*b+3):
            if sudoku[x][y] in promising:
                promising.remove(sudoku[x][y])

    return promising


def dfs(idx):


    if idx == len(zeros):
        for row in sudoku:
            print(*row)
        exit()
    else:
        (i,j) = zeros[idx]
        promising = is_promising(i,j)

        if not promising:
            return

        for prom in promising:
            sudoku[i][j] = prom
            dfs(idx+1)
            sudoku[i][j] = 0
            # promising에서 검사를 할 때 0이여야 promising에 영향을 안 준다.


dfs(0)


"""
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0


0 0 0 0 0 0 0 0 9

0 0 0 0 0 0 0 0 8

0 0 0 0 0 0 0 0 7

0 0 0 0 0 0 0 0 6

0 0 0 0 0 0 0 0 5

0 0 0 0 0 0 0 0 4

0 0 0 0 0 0 0 0 3

0 0 0 0 0 0 0 0 2

0 0 0 0 0 0 0 0 1

"""



