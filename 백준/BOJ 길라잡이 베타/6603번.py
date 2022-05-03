import itertools
import sys


big_data=[]
while True:
    data = list(map(int, sys.stdin.readline().split()))
    if data[0] == 0:
        break
    big_data.append(data)

for i in range(len(big_data)):
    prin = list(itertools.combinations(big_data[i][1:],6))
    for i in prin:
        print(*(i))
    if i != len(big_data)-1:
        print()

"""
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
"""