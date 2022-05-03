"""
3
10
20
40
"""
# import itertools
#
# length = int(input())
# cards = []
# for i in range(length):
#     cards.append(int(input()))
#
#
# answer = 1e9
# for card in itertools.permutations(cards, length):
#     start = card[0]
#     count = 0
#     for i in range(1, length):
#         start += card[i]
#         count += start
#     answer = min(answer, count)
#
# print(answer) 이 솔루션은 시간초과가 난다

#해당 문제는 항상 가장 작은 두 카드 묶음이 합쳐졌을 때 최적의 해를 보장한다.
import heapq

heap = []
for i in range(int(input())):
    heapq.heappush(heap, int(input()))

result = 0

while len(heap) != 1: #힙이 하나 남을 때까지 - 최종적으로 다 합쳐진 힙
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_v = one + two
    result += sum_v
    heapq.heappush(heap, sum_v)

print(result)