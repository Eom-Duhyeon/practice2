import sys

N = int(sys.stdin.readline())
has = [0]*10001
for i in range(N):
    num = int(sys.stdin.readline())
    has[num] += 1

for i in range(len(has)):
    for j in range(has[i]):
        print(i)

# 해당 문제는 pypy3로 제출하면 메모리가 초과된다. 일반적으로 pypy3는 메모리 사용 예측이 어려워서 더 크게 잡힌다.

import sys
n = int(sys.stdin.readline())
cnt = [0]*10001
for i in range(n):
    cnt[int(sys.stdin.readline())] += 1

for i in range(10001):
    for j in range(cnt[i]):
        print(i)
"""
10
5
2
3
1
4
2
3
5
1
7
"""