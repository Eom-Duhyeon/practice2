# import sys
#
# N = int(input())
# l = []
# right = []
# left = []
# for i in range(N):
#     l.append(int(sys.stdin.readline()))
#     right = l.copy()
# right.sort(reverse=True)
# result = []
# print("+")
# left.append(right.pop())
#
# j=1
# k=0
# for i in range (1,N):
#     if k:
#         break
#     while j:
#         if left[-1] == l[i]:
#             result.append(left.pop())
#             print("-")
#             j -= 1
#         elif left[-1] > l[i]:
#             print("NO")
#             k += 1
#         elif left[-1] < l[i]:
#             left.append(right.pop())
#             print("+")



#4 3 6 8 7 5 2 1
# 8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1
import collections

ori = []
n = int(input())
for i in range(n):
    ori.append(int(input()))

left = []
right = collections.deque(sorted(ori))
answer = []
i = 0

while i != n:
    if not left and not right:
        print("NO")
        exit()
    if not left or ori[i] > left[-1]:
        left.append(right.popleft())
        answer.append("+")
    elif left[-1] == ori[i]:
        left.pop()
        answer.append("-")
        i += 1
    elif left[-1] > ori[i] or not right:
        print("NO")
        exit()

for j in answer:
    print(j)


