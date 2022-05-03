n = int(input())
stair = [0]
for i in range(n):
    stair.append(int(input()))
score=[0 for _ in range(n+1)]
if n==1:
    print(stair[1])
elif n==2:
    print(stair[1]+stair[2])
elif n==3:
    print(max(stair[1]+stair[3], stair[2]+stair[3]))
else:
    score[1] = stair[1]
    score[2] = stair[1] + stair[2]
    score[3] = max(stair[1] + stair[3], stair[2] + stair[3])
    for i in range(4, n + 1):
        score[i] = max(stair[i] + score[i - 2], stair[i] + stair[i - 1] + score[i - 3])

    print(score[n])

