"""
5
8 3 7 9 2
3
5 7 9
"""
import sys

n = int(input())
cat = set(map(int, sys.stdin.readline().split()))
m = int(input())
array = list(map(int, sys.stdin.readline().split()))

for k in array:
    if k in cat:
        print("yes",end=" ")
    else:
        print("no", end=" ")

