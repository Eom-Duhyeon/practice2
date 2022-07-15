# import sys
#
# n = int(input())
#
# rope=[]
# for i in range(n):
#     rope.append(int(sys.stdin.readline()))
# rope.sort()
#
# maximum = rope[0]*n
# for i in range(1,n):
#     maximum = max(rope[i]*(n-i),maximum)
#
# print(maximum)

"""
2
10
15
출력 : 20
"""

# 로프의 길이가 같을 때에도 문제되지 않는다. ropes[i]==ropes[i+1] 일 때에도 최댓값은 이미 max_v에 찍혔고 i+1일 때 무의미한 검사를 할 뿐이다.

import sys

ropes = []
n = int(sys.stdin.readline())
for i in range(n):
    ropes.append(int(sys.stdin.readline()))

ropes.sort()
max_v = ropes[0]*n
for i in range(1, n):
    if ropes[i]*(n-i) > max_v:
        max_v = ropes[i]*(n-i)

print(max_v)