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
# import sys
#
# big_data = []
# while True:
#     data = list(map(int, sys.stdin.readline().split()))
#     if data[0] == 0:
#         break
#     big_data.append(data)
#
# n = len(big_data)
#
# def comb(arr, r):
#     result = []
#     if len(arr) < r:
#         return result
#     if r == 1:
#         for i in arr:
#             result.append([i])
#     elif r > 1:
#         for i in range(len(arr) - r + 1):
#             for j in comb(arr[i+1:], r - 1):
#                 result.append([arr[i]]+j)
#
#     return result
#
#
# for i in range(len(big_data)):
#     for j in comb(big_data[i][1:], 6):
#         print(*(j))
#
#     if i != len(big_data)-1:
#         print()




# import itertools
# import sys
#
# big_data = []
# while True:
#     data = list(map(int, sys.stdin.readline().split()))
#     if data[0] == 0:
#         break
#     big_data.append(data)
#
# n = len(big_data)
#
# for i in range(n):
#     for j in itertools.combinations(big_data[i][1:], 6):
#         print(*(j))
#     if i != n:
#         print()

# 결론
# def comb(arr, r):
#     result = []
#
#     if len(arr) < r:
#         return result
#
#     if r == 1:
#         for i in arr:
#             result.append([i])
#     elif r > 1:
#         for i in range(len(arr) - r + 1):
#             for j in comb(arr[i+1:], r-1):
#                 result.append([arr[i]]+j)
#     return result
#
# arr = [1,2,3,4,5]
# print(comb(arr, 3))