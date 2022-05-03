
"""
예제 입력 1
10 4200
1
5
10
50
100
500
1000
5000
10000
50000

10 4790
1
5
10
50
100
500
1000
5000
10000
50000
"""
import sys

n, target = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline()))

count = 0
while target:
    a = target//coins[-1]
    count += a
    target -= a*coins[-1]
    coins.pop()

print(count)
