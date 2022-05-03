import sys

n = int(input())

wi = []
for i in range(n):
    wi.append(int(sys.stdin.readline()))

dp = [0]*(n+1)

if n==1:
    dp[0] = wi[0]
elif n==2:
    dp[1] = wi[0] + wi[1]
elif n==3:
    dp[2] = max(wi[0]+wi[1], wi[0]+wi[2], wi[1]+wi[2])
elif n==4:
    dp[3] = max(wi[0]+wi[1]+wi[3], wi[0]+wi[2]+wi[3], wi[1]+wi[2])
else:
    dp[0] = wi[0]
    dp[1] = wi[0] + wi[1]
    dp[2] = max(wi[0] + wi[1], wi[0] + wi[2], wi[1] + wi[2])
    dp[3] = max(wi[0] + wi[1] + wi[3], wi[0] + wi[2] + wi[3], wi[1] + wi[2])
    for i in range(4, n):
        dp[i] = max(dp[i-1], wi[i]+wi[i-1]+dp[i-3], wi[i]+dp[i-2])
print(dp[n-1])


"""
6
6
10
13
9
8
1
"""