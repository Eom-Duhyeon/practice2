"""
입력 예시
5 3
1 2 5 4 3
5 5 6 6 5
출력 예시
26
"""
import sys

a, b = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l1.sort()
l2.sort(reverse=True)
for i in range(b):
    if l1[i] >= l2[i]:
        break
    l1[i] = l2[i]

print(sum(l1))

