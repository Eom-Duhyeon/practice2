"""
6
10 20 10 30 20 50

dp로 풀었다. i보다 작은 j에 대해 만약 data[i]가 i번째까지 순회하는 j에 대해 data[j]보다 크다면 max(dp[j]+1, dp[i])
즉 가장 큰 dp[j] +1
"""
import sys

n = int(input())
data = list(int(x) for x in sys.stdin.readline().split())
dp = [1]*n

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))