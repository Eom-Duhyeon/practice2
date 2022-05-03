"""
입력 예시1
2 15
2
3
출력 예시1
5
"""

n, m = map(int, input().split())
coins=[]
big = 10000
dp =[big]*10001
dp[0] = 0 # 아주 중요
for _ in range(n):
    coins.append(int(input()))

for i in range(n):
    for j in range(coins[i], m+1):
        if dp[j-coins[i]] != big:
            dp[j] = min(dp[j], dp[j-coins[i]]+1)

if dp[m] == big:
    print(-1)
else:
    print(dp[m])