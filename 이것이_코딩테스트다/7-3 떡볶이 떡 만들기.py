

n,m = map(int, input().split()) #n은 떡 개수, m은 길이
cake = list(map(int, input().split()))

start = 0
end = max(cake)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in cake:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid +1

print(result)

"""
입력 예시
4 6
19 15 10 17
출력 예시
15
"""

