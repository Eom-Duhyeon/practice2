a, b = map(int, input().split())

prim = [True]*1000001
prim[0], prim[1] = False, False
for i in range(2, 1002):
    if prim[i] == True:
        for j in range(i+i, 1000001, i):
            prim[j] = False

for i in range(a, b+1):
    if prim[i] == True:
        print(i)