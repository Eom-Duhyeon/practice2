# N = int(input())
# A = [int(x) for x in input().split()]
# A.sort()
# B = [int(y) for y in input().split()]
#
# answer = 0
# for i in range(N):
#     answer += A[0] * max(B)
#     del A[0]
#     B.pop(B.index(max(B)))
#
# print(answer)

n = int(input())
li_n = list(map(int, input().split()))
li_m = list(map(int, input().split()))
li_n.sort()

answer = 0
for i in range(n):
    answer += max(li_m) * li_n[i]
    del li_m[li_m.index(max(li_m))]

print(answer)

"""
5
1 1 1 6 0
2 7 8 3 1

3
1 1 3
10 30 20

9
5 15 100 31 39 0 0 3 26
11 12 13 2 3 4 5 9 1
"""