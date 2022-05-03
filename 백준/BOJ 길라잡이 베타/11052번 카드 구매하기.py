"""
DP를 이용하여 풀 수 있다. dp[i] = max(dp[i-j] + cardpack[j], dp[i])를 i보다 작은 모은 j에 대해 검사한다.(0은 의미 없으니까 1부터)


"""

import sys

n = int(input())

cardpack = [0] + list(int(x) for x in sys.stdin.readline().split())
dp = [0]*(n+1)

dp[1] = cardpack[1]

for i in range(2, n+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + cardpack[j]:
            dp[i] = dp[i-j] + cardpack[j]

print(dp[n])

"""
4
1 5 6 7

5
10 9 8 7 6

10
1 1 2 3 5 8 13 21 34 55


"""
