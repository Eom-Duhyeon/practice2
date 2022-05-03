import sys

n = int(input())

rope=[]
for i in range(n):
    rope.append(int(sys.stdin.readline()))
rope.sort()

maximum = rope[0]*n
for i in range(1,n):
    maximum = max(rope[i]*(n-i),maximum)

print(maximum)
