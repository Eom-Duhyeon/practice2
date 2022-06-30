# a, b = map(int, input().split())
#
# prim = [True]*1000001
# prim[0], prim[1] = False, False
# for i in range(2, 1002):
#     if prim[i] == True:
#         for j in range(i+i, 1000001, i):
#             prim[j] = False
#
# for i in range(a, b+1):
#     if prim[i] == True:
#         print(i)


l, r = map(int, input().split())

prim = [False]*2 + [True]*(r-1)

for i in range(2, int(r**0.5)+1):
    if prim[i]:
        for j in range(i+i, r+1, i):
            prim[j] = False

for i in range(l, r+1):
    if prim[i]:
        print(i)

