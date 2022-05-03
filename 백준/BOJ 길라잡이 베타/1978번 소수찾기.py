import sys

prim = [True]*1001
prim[0] = False
prim[1] = False
for i in range(2, len(prim)):
    if prim[i]==True:
        for j in range(i+i,1001,i):
            prim[j] = False

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
answer=0
for i in data:
    if prim[i] == True:
        answer +=1

print(answer)