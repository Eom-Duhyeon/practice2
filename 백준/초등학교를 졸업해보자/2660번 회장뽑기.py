n = int(input())

mat = [[1000 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    mat[i][i] = 0
while 1:
    a, b = map(int, input().split())
    if a== -1:
        break
    mat[a][b]=1
    mat[b][a]=1

for k in range(1,n+1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j])

ans1=0
ans_help=[]
ans2=0
ans3=[]

for i in range(1,n+1):
    ans_help.append(max(mat[i][1:n+1]))

ans1 = min(ans_help)
ans2 = ans_help.count(ans1)

print(ans1,ans2)
for i in range(0,n):
    if ans_help[i] == ans1:
        ans3.append(i+1)

print(*ans3)



