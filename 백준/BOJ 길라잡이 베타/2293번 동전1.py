# import sys
#
# sys.setrecursionlimit(100000)
#
# n, target = map(int, input().split())
# candidates = []
# for i in range(n):
#     candidates.append(int(input()))
#
#
# count = 0
#
# def dfs(csum, index):
#     if csum == 0:
#         global count
#         count += 1
#         return
#     elif csum < 0:
#         return
#
#     for i in range(index, n):
#         dfs(csum-candidates[i], i)
#
#
# dfs(target, 0)
# print(count)

# 해당 문제를 위의 방식으로 풀면 재귀에러가 난다. dp를 사용하여 더 쉽게 풀 수 있다.

n, k = map(int, input().split())
candidates= []
dp=[0]*(k+1)
dp[0] = 1
coins = []
for i in range(n):
    coins.append(int(input()))

for i in coins:
    for j in range(1, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[k])