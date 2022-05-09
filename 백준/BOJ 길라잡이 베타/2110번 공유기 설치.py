"""
5 3
1
2
8
4
9

출력 :
3
"""


m, c = map(int, input().split())

data = []
for i in range(m):
    data.append(int(input()))
data.sort()
start = 1
end = data[-1] - data[0]
answer = 0

while start <= end:
    mid = (start + end)//2
    tmp = 1e9
    count = 1
    current = data[0]
    for i in range(1, m):
        if current + mid <= data[i]:
            count += 1
            tmp = min(tmp, data[i] - current)
            current = data[i]

    if count < c:
        end = mid -1
    else:
        start = mid +1
        answer = max(answer, tmp)

print(answer)


