n = 4
times = [2,3]

def solution(n, times):
    # 다이나믹 프로그래밍을 통해 문제를 해결할 수 있다.
    # 모든 정답은 줄을 한 하나씩 자르는 경우 걸리는 시간 즉 (n-1)*time[0] 보다 작거나 같다.
    dp = [0]*(n+1)
    for i in range(n+1):
        dp[i] = (n-1)*times[0]
    if len(times) == 1:
        return dp[n]

    for i in range(len(times)):
        for j in range(i+2,n+1):
            dp[j] = min(dp[j], dp[j-i]+times[i])
    answer = dp[n]
    return answer

print(solution(n, times))