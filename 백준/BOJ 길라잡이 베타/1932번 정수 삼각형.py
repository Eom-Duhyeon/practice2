
# import sys
#
# n = int(input())
# tri = []
#
# for i in range(n):
#     tri.append(list(int(x) for x in sys.stdin.readline().split()))
#
# k = 2
# for i in range(1, n):
#     for j in range(k):
#         if j == 0:
#             tri[i][j] += tri[i-1][0]
#         elif j == i:
#             tri[i][j] += tri[i-1][j-1]
#         else:
#             tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])
#     k += 1
#
# print(max(tri[n-1]))

"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

"""
import sys

n = int(sys.stdin.readline())
tri = []
for i in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            tri[i][j] += tri[i-1][0]
        elif j == i:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[n-1]))
