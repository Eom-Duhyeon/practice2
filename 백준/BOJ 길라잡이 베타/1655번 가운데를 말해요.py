#max 힙과 min힙 두 개를 준비해서 작은 것은 max힙에, 큰 것은 min 힙에 넣는다
# 두 힙이 비었다면 하나를 max힙에 넣고 max힙과 min힙 중 더 크기가 큰 것을 반환한다. pop은 하지 않는다
#만약 두 힙의 크기가 같다면 max힙껄 보여준다
#원소를 삭제하지 않고 힙 값을 보고 싶다면 인덱스 0으로 접근하면 된다.
import heapq
import sys

n = int(sys.stdin.readline())

#빅가이즈가 민 힙 스몰 가이즈가 맥스 힙
big_guys = []
small_guys = []

current = int(input())
heapq.heappush(small_guys, (-current, current))
print(current)

for i in range(1, n):
    a = int(sys.stdin.readline())

    if a >= current:

        if len(big_guys) > len(small_guys):

            heapq.heappush(big_guys, a)

            buf = heapq.heappop(big_guys)

            heapq.heappush(small_guys, (-buf, buf))

        else:

            heapq.heappush(big_guys, a)

    else:

        if len(big_guys) < len(small_guys):

            heapq.heappush(small_guys, (-a, a))

            buf1, buf2 = heapq.heappop(small_guys)

            heapq.heappush(big_guys, buf2)

        else:

            heapq.heappush(small_guys, (-a, a))


    if len(small_guys) >= len(big_guys):
        current = small_guys[0][1]
    elif len(small_guys) < len(big_guys):
        current = big_guys[0]
    print(current)




"""
7
1
5
2
10
-99
7
5
"""