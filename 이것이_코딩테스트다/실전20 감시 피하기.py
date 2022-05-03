"""
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

출력
YES

"""
import itertools

n = int(input())
hallway =[]

for i in range(n):
    hallway.append(list(input().split()))
# n = 4
# hallway=[['S', 'S', 'S', 'T'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['T', 'T', 'T', 'X']]

students = []
wall_cand = []
for i in range(n):
    for j in range(n):
        if hallway[i][j] == "S":
            students.append((i,j))
        elif hallway[i][j] == "X":
            wall_cand.append((i,j))

def save(i, j):
    k = i
    while k != -1:
        if hallway[k][j] == "T":
            return False
        elif hallway[k][j] == "O":
            break
        k-=1

    k = i
    while k != n:
        if hallway[k][j] == "T":
            return False
        elif hallway[k][j] == "O":
            break
        k += 1

    l = j
    while l != n:
        if hallway[i][l] == "T":
            return False
        elif hallway[i][l] == "O":
            break
        l += 1

    l = j
    while l != -1:
        if hallway[i][l] == "T":
            return False
        elif hallway[i][l] == "O":
            break
        l -= 1

    return True



for walls in itertools.combinations(wall_cand, 3):
    for x, y in walls:
        hallway[x][y] = "O"

    life = True
    for x, y in students:
        if not save(x, y):
            life = False

    if life == True:
        print("YES")
        exit()

    for x, y in walls:
        hallway[x][y] = "X"

print("NO")