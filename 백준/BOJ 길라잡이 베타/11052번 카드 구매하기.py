"""
DP를 이용하여 풀 수 있다. dp[i] = max(dp[i-j] + cardpack[j], dp[i])를 i보다 작은 모은 j에 대해 검사한다.(0은 의미 없으니까 1부터)


"""

# import sys
#
# n = int(input())
#
# cardpack = [0] + list(int(x) for x in sys.stdin.readline().split())
# dp = [0]*(n+1)
#
# dp[1] = cardpack[1]
#
# for i in range(2, n+1):
#     for j in range(1, i+1):
#         if dp[i] < dp[i-j] + cardpack[j]:
#             dp[i] = dp[i-j] + cardpack[j]
#
# print(dp[n])
import sys

"""
4
1 5 6 7

5
10 9 8 7 6

10
1 1 2 3 5 8 13 21 34 55

"""

n = int(sys.stdin.readline())
dp = [0]*(n+1)
cards = [0] + list(map(int, sys.stdin.readline().split())) # 이렇게 안 하면 dp[i] = dp[i-j] + cards[j-1] 꼴로
dp[1] = cards[1]

for i in range(2, n+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + cards[j]:
            dp[i] = dp[i-j] + cards[j]

print(dp[n])
