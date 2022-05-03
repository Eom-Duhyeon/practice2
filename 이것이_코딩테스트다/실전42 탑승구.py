# n = int(input())
# m = int(input())
# gate = [i+1 for i in range(n)]
# airplanes = []
# for i in range(m):
#     airplanes.append(int(input())-1)
#
# for k in range(m):
#     i = airplanes[k]
#     for j in range(i, n):
#         gate[j] -= 1
#     for j in (0, i):
#         if gate[j] > gate[i]:
#             gate[j] = gate[i]
#
#     for j in range(n):
#         if gate[j] < 0:
#             print(k)
#             exit()

#서로소 해결법

#해당 코드는 답이 나오는 즉시 input까지 차단한다.

def find_P(parent, x):
    if parent[x] != x:
        return find_P(parent, parent[x])
    else:
        return x

def union_P(parent, a, b):
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

g = int(input())
p = int(input())
parent = [0] * (g + 1)

for i in range(1, g + 1):
    parent[i] = i

result = 0
for _ in range(p):
    data = find_P(parent, int(input()))
    if data == 0:
        break
    union_P(parent, data, data - 1)
    result += 1

print(result)