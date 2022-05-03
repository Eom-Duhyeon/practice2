import sys

l = [True for i in range(1000001)]
nn=0

#1000000에 대한 검사는 그 루트값인 1000까지만 해도 충분하다 1000*1000 면 1000000니까

for i in range(2, 1001):
    if l[i] == True:
        for j in range(i * 2, 1000001, i):
            l[j] = False

while True:
    n=int(sys.stdin.readline())
    if n == 0:
        break

    for k in range(3, n):
        if l[k] and l[n-k]:
            print(n, "=", k, "+", n-k)
            break

