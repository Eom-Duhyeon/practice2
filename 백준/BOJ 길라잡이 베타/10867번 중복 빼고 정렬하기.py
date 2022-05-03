import sys
N = int(input())

a = [int(x) for x in sys.stdin.readline().split()]
a = set(a)
print(*(sorted(a)))