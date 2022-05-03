import sys

N=int(input())
arr1 = list(map(int, sys.stdin.readline().split()))
arr1.sort()
n=int(input())
arr2 = list(map(int, sys.stdin.readline().split()))

# def BSF(k, start, fin):
#     while start <= fin:
#         mid = (start+fin)//2
#         if k == arr1[mid]:
#             return 1
#         elif k < arr1[mid]:
#             fin = mid - 1
#         else :
#             start = mid + 1
#     return 0

def BSF(k, start, fin):
    if start > fin:
        return 0
    mid = (start + fin) // 2
    if k == arr1[mid]:
        return 1

    elif k < arr1[mid]:
        BSF(k, start, mid-1)
    else:
        BSF(k, mid+1, fin)


for i in arr2:
    if BSF(i, 0, N-1):
        print(1, end=' ')
    else:
        print(0, end=' ')
# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10
