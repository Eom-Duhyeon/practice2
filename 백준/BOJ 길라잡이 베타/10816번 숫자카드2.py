# import sys
#
# N = int(input())
# a = [int(x) for x in sys.stdin.readline().split()]
# dict={}
# for k in a:
#     if k in dict:
#         dict[k] += 1
#     else:
#         dict[k] = 1
#
# n = int(input())
# b = [int(x) for x in sys.stdin.readline().split()]
# c=[]
# for i in b:
#     if i in dict:
#         c.append(dict[i])
#     else:
#         c.append(0)
#
# print(*(c))


n = int(input())
list_n = list(map(int, input().split()))
dic = dict()
for i in list_n:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

m = int(input())
lis_m = list(map(int, input().split()))
for i in lis_m:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")

"""
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
"""