"""
입력 예시
4
1 3 1 5
출력 예시
8
"""

n = int(input())
array = list(map(int, input().split()))
dp = [0]*101

for i in range(n):
    dp[0] = array[0]
    dp[1] = max(array[0], array[1])
    dp[i] = max(dp[i-1], dp[i-2]+array[i])

print(dp[n-1])
