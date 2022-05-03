import collections

n, k = map(int, input().split())

data = [0]*100001

qu = collections.deque()
qu.append(n)
while qu:
    m = qu.popleft()
    if m == k:
        print(data[m])
        break
    else:
        for i in (m-1, m+1, m*2):
            if 0 <= i < 100001 and not data[i]:
                data[i] = data[m] + 1
                qu.append(i)
