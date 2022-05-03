import sys

N = int(sys.stdin.readline())
has = [0]*10001
for i in range(N):
    num = int(sys.stdin.readline())
    has[num] += 1

for i in range(len(has)):
    for j in range(has[i]):
        print(i)
