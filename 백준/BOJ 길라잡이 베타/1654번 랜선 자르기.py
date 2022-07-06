# n, target = map(int, input().split())
#
# cables = []
# for i in range(n):
#     cables.append(int(input()))
#
#
# start = 1 # start 를 0으로 했을 때 런타임 에러 발생
# end = max(cables)
#
# while start <= end:
#     mid = (start+end)//2
#     num = 0
#     for cable in cables:
#         num += cable//mid
#     if num >= target:
#         start = mid + 1
#     else:
#         end = mid - 1
#
# print(end)


"""
4 11
802
743
457
539
"""
import sys

k, n = map(int, sys.stdin.readline().split()) #k는 이미 가지고 있는. n은 필요한 줄 수
cables = []
for i in range(k):
    cables.append(int(sys.stdin.readline()))

start = 1
end = max(cables)

while start <= end:
    mid = (start+end)//2
    num = 0
    for cable in cables:
        num += cable//mid
    if num < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)