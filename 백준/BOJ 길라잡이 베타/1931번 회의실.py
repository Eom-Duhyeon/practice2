import sys

n = int(input())

data = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    data.append((a, b))

data.sort(key=lambda x: (x[1],x[0]))

count = 0
fin = 0
for i,j in data:
    if i >= fin:
        count += 1
        fin = j

print(count)

"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

"""