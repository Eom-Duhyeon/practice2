
n, target = map(int, input().split())

cables = []
for i in range(n):
    cables.append(int(input()))


start = 1 # start 를 0으로 했을 때 런타임 에러 발생
end = max(cables)

while start <= end:
    mid = (start+end)//2
    num = 0
    for cable in cables:
        num += cable//mid
    if num >= target:
        start = mid + 1
    else:
        end = mid - 1

print(end)


"""
4 11
802
743
457
539
"""