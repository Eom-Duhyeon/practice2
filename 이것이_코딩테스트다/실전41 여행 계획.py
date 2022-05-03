n, m = map(int, input().split())
travels = []
for i in range(n):
    travels.append(list(map(int, input().split())))
plans = list(map(int, input().split()))

parent = [int(i) for i in range(n)]

def find_P(parent, x):
    if parent[x] != x:
        return find_P(parent, parent[x])
    else:
        return x

def union_P(parent, a, b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(n):
    for j in range(n):
        if travels[i][j] == 1:
            union_P(parent, find_P(parent, i), find_P(parent, j))

answer = "YES"

for i in range(1, m):
    if parent[plans[i]-1] != parent[plans[0]-1]:
        answer = "NO"
        break

print(answer)