# import collections
# import sys
#
# N = int(input())
# for i in range(N):
#     order = input()
#     length = int(input())
#     arr = collections.deque(sys.stdin.readline().rstrip()[1:-1].split(","))
#
#     error = False
#     cnt = 0
#
#     if length == 0:
#         arr = []
#
#     for j in order:
#         if j == "R":
#             cnt += 1
#         elif j == "D":
#             if arr:
#                 if cnt % 2 == 0:
#                     arr.popleft()
#                 else:
#                     arr.pop()
#             else:
#                 print("error")
#                 error = True
#                 break
#
#     if not error:
#         if cnt%2 == 0:
#             print("[" + ",".join(arr) + "]")
#         else:
#             arr.reverse()
#             print("[" + ",".join(arr) + "]")


"""
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]


출력
[2,1]
error
[1,2,3,5,8]
error

"""
import collections
import sys

for i in range(int(input())):
    orders = sys.stdin.readline().rstrip()
    length = int(input())
    arr = collections.deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    if orders.count("D") > length:
        print("error")
        continue

    cnt = 0
    for i in orders:
        if i == "R":
            cnt += 1
        else:
            if cnt % 2 != 0:
                arr.pop()
            else:
                arr.popleft()
    if cnt % 2 == 0:
        print("[",",".join(str(i) for i in arr) ,"]",sep="")
    else:
        arr.reverse()
        print("[", ",".join(str(i) for i in arr), "]", sep="")

    #