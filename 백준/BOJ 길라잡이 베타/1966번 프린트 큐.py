# import collections
# import heapq
# import sys
#
# # 꼭 데이터와 인덱스를 튜플로 묶을 필요 없다 각각 pop하는 방법이 더 편할 수도 있다
#
# n = int(input())
# for i in range(n):
#     m, k = map(int, input().split()) # m 은 문서의 수, k은 몇 번째 문서인지
#     data = collections.deque(int(x) for x in sys.stdin.readline().split())
#     index = collections.deque(int(x) for x in range(1,m+1))
#     index[k] = 102
#     maxi = max(data)
#     answer = 0
#     while True:
#         if data[0] == maxi:
#             if index[0] == 102:
#                 answer += 1
#                 print(answer)
#                 break
#             else:
#                 data.popleft()
#                 index.popleft()
#                 maxi = max(data)
#                 answer += 1
#         else:
#             data.append(data.popleft())
#             index.append(index.popleft())
#
#             heapq.heapify()

"""
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
"""

import collections
import sys

for i in range(int(input())):
    length, idx = map(int, sys.stdin.readline().split())
    printer = collections.deque([int(x) for x in sys.stdin.readline().split()])
    orders = collections.deque([int(x) for x in range(length)])
    max_v = max(printer)
    answer = 0
    while printer:
        if printer[0] == max_v:
            if orders[0] == idx:
                answer += 1
                print(answer)
                break
            else:
                printer.popleft()
                orders.popleft()
                answer += 1
                max_v = max(printer)
        else:
            printer.append(printer.popleft())
            orders.append(orders.popleft())







