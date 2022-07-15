# import sys
#
# n = int(input())
#
# wi = []
# for i in range(n):
#     wi.append(int(sys.stdin.readline()))
#
# dp = [0]*(n+1)
#
# if n==1:
#     dp[0] = wi[0]
# elif n==2:
#     dp[1] = wi[0] + wi[1]
# elif n==3:
#     dp[2] = max(wi[0]+wi[1], wi[0]+wi[2], wi[1]+wi[2])
# elif n==4:
#     dp[3] = max(wi[0]+wi[1]+wi[3], wi[0]+wi[2]+wi[3], wi[1]+wi[2])
# else:
#     dp[0] = wi[0]
#     dp[1] = wi[0] + wi[1]
#     dp[2] = max(wi[0] + wi[1], wi[0] + wi[2], wi[1] + wi[2])
#     dp[3] = max(wi[0] + wi[1] + wi[3], wi[0] + wi[2] + wi[3], wi[1] + wi[2])
#     for i in range(4, n):
#         dp[i] = max(dp[i-1], wi[i]+wi[i-1]+dp[i-3], wi[i]+dp[i-2])
# print(dp[n-1])


"""
6
6
10
13
9
8
1
"""
import sys

n = int(sys.stdin.readline())
grapes = []
for i in range(n):
    grapes.append(int(sys.stdin.readline()))

if n < 5:
    if n == 1:
        print(grapes[0])
    elif n == 2:
        print(grapes[0]+grapes[1])
    elif n == 3:
        print(max(grapes[0]+grapes[1], grapes[2]+grapes[1], grapes[0]+grapes[2]))
    elif n == 4:
        print(max(grapes[0]+grapes[1]+grapes[3], grapes[0]+grapes[3]+grapes[2], grapes[1]+grapes[2]))
else:
    dp = [0]*n
    dp[0] = grapes[0]
    dp[1] = grapes[0]+grapes[1]
    dp[2] = max(grapes[0]+grapes[1], grapes[2]+grapes[1], grapes[0]+grapes[2])
    dp[3] = max(grapes[0]+grapes[1]+grapes[3], grapes[0]+grapes[3]+grapes[2], grapes[1]+grapes[2])
    for i in range(4, n):
        dp[i] = max(dp[i-1], grapes[i]+dp[i-2], grapes[i]+grapes[i-1]+dp[i-3])
    print(dp[n-1])
