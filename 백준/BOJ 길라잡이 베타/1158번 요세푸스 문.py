# 큐를 이용하여 풀 수 있다. k의 배수번째마다 pop을 시켜서 answer에 넣고 k번째가 아닐 때에는 다시 큐에 push한다.
# import collections
#
# m, k = map(int, input().split())
# q = collections.deque()
# for i in range(1,m+1):
#     q.append(i)
#
# ans = []
#
#
# i=0
# while q:
#     i+=1
#     if i%3==0:
#         ans.append(q.popleft())
#     else:
#         a = q.popleft()
#         q.append(a)
#
# print("<", ', '.join(str(i) for i in ans), ">", sep="")

#틀린 이유를 알 수 없다.

# m, k = map(int, input().split())
#
# answer = []
# deadman = [x for x in range(1, m+1)]
#
# num = k-1
# for i in range(m):
#     if len(deadman) > num:
#         answer.append(deadman.pop(num))
#         num += k-1
#     else:
#         num %= len(deadman)
#         answer.append(deadman.pop(num))
#         num += k-1
# print("<", ', '.join(str(i) for i in answer), ">", sep="")
import collections

n, k = map(int, input().split())

men = collections.deque([int(x) for x in range(1, n+1)])
answer = []

count = 0
while men:
    count += 1
    if count == k:
        answer.append(men.popleft())
        count = 0
    else:
        men.append(men.popleft())
print("<", ", ".join(str(i) for i in answer), ">", sep="")
# num = k-1
# for i in range(n):
#     if len(men) > num:
#         answer.append(men.pop(num))
#         num += k-1
#     else:
#         num %= len(men)
#         answer.append(men.pop(num))
#         num += k-1
# print("<", ", ".join(str(i) for i in answer), ">", sep="")

