import heapq

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

hp = []

for i in range(n):
    for j in range(i+1, n):
        cost = min(abs(data[i][0]-data[j][0]), abs(data[i][1]-data[j][1]), abs(data[i][2]-data[j][2]))
        heapq.heappush(hp, (cost, i, j))



parent = [i for i in range(n)]

def fin_P(parent, x):
    if parent[x] != x:
        return fin_P(parent, parent[x])
    else:
        return x


def union_P(parent, a, b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


total = 0


for i in range((n*(n-1))//2):
    cost, a, b = heapq.heappop(hp)
    a = fin_P(parent, a)
    b = fin_P(parent, b)
    if a == b:
        continue

    union_P(parent, a, b)
    total += cost

print(total)
