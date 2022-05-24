# import sys
#
# N=int(input())
# arr1 = list(map(int, sys.stdin.readline().split()))
# arr1.sort()
# n=int(input())
# arr2 = list(map(int, sys.stdin.readline().split()))
#
# # def BSF(k, start, fin):
# #     while start <= fin:
# #         mid = (start+fin)//2
# #         if k == arr1[mid]:
# #             return 1
# #         elif k < arr1[mid]:
# #             fin = mid - 1
# #         else :
# #             start = mid + 1
# #     return 0
#
# def BSF(k, start, fin):
#     if start > fin:
#         return 0
#     mid = (start + fin) // 2
#     if k == arr1[mid]:
#         return 1
#
#     elif k < arr1[mid]:
#         BSF(k, start, mid-1)
#     else:
#         BSF(k, mid+1, fin)
#
#
# for i in arr2:
#     if BSF(i, 0, N-1):
#         print(1, end=' ')
#     else:
#         print(0, end=' ')
# # 5
# # 6 3 2 10 -10
# # 8
# # 10 9 -5 2 3 4 5 -10

# 1920번 수 찾기와 완전히 똑같은 문제

"""
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
"""
import sys

n = int(input())
li_n = list(map(int, sys.stdin.readline().split()))
li_n.sort()
m = int(input())
li_m = list(map(int, sys.stdin.readline().split()))

def check(i):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start+end)//2
        if li_n[mid] == i:
            return True
        if li_n[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    return False

for i in li_m:
    if check(i):
        print(1, end=" ")
    else:
        print(0, end=" ")