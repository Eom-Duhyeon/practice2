"""
https://programmers.co.kr/learn/courses/30/lessons/42891
입출력:
food_times	k	result
[3, 1, 2]	5	1
"""
import heapq
import operator

food_times = [3, 1, 2]
k = 5
# 브루트 포스 실패 : 효율성 미달


def solution(food_times, k):
    n = len(food_times)
    if sum(food_times) <= k:
        return -1
    q=[]
    for i in range(n):
        heapq.heappush(q,(food_times[i], i+1))

    sum_val = 0 # 먹기 위해 사용한 시간
    prev = 0 #이전 음식을 먹은 시간

    while sum_val + ((q[0][0] - prev) * n) <= k:
        now = heapq.heappop(q)[0] #이렇게 pop한 일부만 가져올 수도 있다
        sum_val += (now - prev) * n
        n -= 1
        prev = now

    result = sorted(q, key = lambda x: x[1])
    return result[(k-sum_val) % n][1]





print(solution(food_times, k))