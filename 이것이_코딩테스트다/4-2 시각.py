"""
입력 예시
5
출력 예시
11475
"""

N = int(input())

count = 0
for i in range(N+1): # 0시도 생각해야
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)