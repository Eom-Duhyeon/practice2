import itertools
import sys

length, target = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
answer = 0
for i in range(1, length+1):
    sub = list(itertools.combinations(data, i))
    for j in sub:
        if sum(j) == target:
            answer += 1

print(answer)



