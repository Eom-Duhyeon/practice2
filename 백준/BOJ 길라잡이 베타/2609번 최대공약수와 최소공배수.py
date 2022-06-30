# import sys
#
# #import math를 통해 gcd lcm 함수를 불러올 수도 있다
#
# a, b = map(int, sys.stdin.readline().split())
#
# a, b = max(a,b), min(a,b)
#
# def gcd(a,b):
#     if a % b == 0:
#         return b
#     else :
#         return gcd(b, a % b)
#
# print(int(gcd(a, b)))
# print(int(a * b / gcd(a, b)))

a, b = map(int, input().split())

if b > a:
    a, b = b, a

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(int(gcd(a, b)))
print(int(a*b / gcd(a, b)))

