"""
10
3 5 3 6 3 4 10 4 5 2
"""
import sys

n = int(input())
data = list(map(int, sys.stdin.readline().split()))
answer = 0
l = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if data[j]-data[i] == data[k] - data[j]:
                answer += 1
                l.append([data[i], data[j], data[k]])

print(answer)
print(l)