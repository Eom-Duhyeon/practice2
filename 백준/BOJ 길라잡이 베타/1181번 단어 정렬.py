import sys
import heapq
N = int(input())
answer=[]
for i in range(N):
    answer.append(sys.stdin.readline().strip())

answer=list(set(answer))
answer.sort()
answer.sort(key=len) # 이것만 중요

for j in answer:
    print(j)


# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours