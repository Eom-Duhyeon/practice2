import heapq

n, m = map(int, input().split())
hp=[]
whole = 0
for i in range(m):
    a, b, cost = map(int, input().split())
    heapq.heappush(hp, (cost, a, b))
    whole += cost

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


minimum_cost = 0

for i in range(m):
    cost, a, b = heapq.heappop(hp)
    a = fin_P(parent, a)
    b = fin_P(parent, b)
    if a == b:
        continue
    else:
        union_P(parent, a, b)
        minimum_cost += cost

print(whole - minimum_cost)