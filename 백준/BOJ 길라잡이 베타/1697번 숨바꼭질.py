import collections

n, k = map(int, input().split())

qu = collections.deque()
qu.append(n)

numbers = [0]*100001

while qu:
    now = qu.popleft()
    if now == k:
        print(numbers[now])
        break

    for i in (now-1, now+1, now*2):
        if 0 <= i < 100001 and not numbers[i]: #bfs다보니까 자동으로 가장 가까운 루트가 먼저
            numbers[i] = numbers[now] + 1
            qu.append(i)





