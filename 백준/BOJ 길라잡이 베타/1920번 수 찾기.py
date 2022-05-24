#그냥은 시간초과에 걸린다.
# n = int(input())
# n_list = list(map(int, input().split(' ')))
# n_list.sort()
#
# m = int(input())
# targets = list(map(int, input().split(' ')))
#
#
# def binary(target):
#     left = 0
#     right = n - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if n_list[mid] == target:
#             return True
#
#         if target < n_list[mid]:
#             right = mid-1
#         elif target > n_list[mid]:
#             left = mid + 1
#
#
# for i in range(m):
#     if binary(targets[i]):
#         print(1)
#     else:
#         print(0)

import sys

n = int(input())
list_n = list(map(int, sys.stdin.readline().split()))
list_n.sort()
m = int(input())
list_m = list(map(int, sys.stdin.readline().split()))

def binary_check(target):
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2
        if list_n[mid] == target:
            return True

        if list_n[mid] > target:
            right = mid -1
        else:
            left = mid + 1

    return False

for i in list_m:
    if binary_check(i):
        print(1)
    else:
        print(0)
