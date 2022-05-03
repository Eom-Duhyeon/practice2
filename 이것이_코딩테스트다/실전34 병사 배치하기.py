length = int(input())
soldier = list(map(int, input().split()))
dp = [1 for _ in range(length)]

for i in range(1, length):
    for j in range(i):
        if soldier[j] > soldier[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(length - max(dp))