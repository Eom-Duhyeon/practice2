#
# n = int(input())
#
# zero = [1, 0, 1]
# one = [0, 1, 1]
# def fibo(n):
#     length = len(zero)
#     if n < length:
#         print(zero[n], one[n], sep=" ")
#     else:
#         for i in range(length, n+1):
#             zero.append(zero[i-1]+zero[i-2])
#             one.append(one[i-1]+one[i-2])
#         print(zero[n], one[n], sep=" ")
#
# for i in range(n):
#     fibo(int(input()))
import sys

zero = [1, 0]
one = [0, 1]

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n < len(zero):
        print(zero[n], one[n], sep=" ")
    else:
        for j in range(len(zero), n+1):
            zero.append(zero[j-1]+zero[j-2])
            one.append(one[j-1]+one[j-2])
        print(zero[n], one[n], sep=" ")



