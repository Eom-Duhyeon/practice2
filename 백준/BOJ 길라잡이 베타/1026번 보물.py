N = int(input())
A = [int(x) for x in input().split()]
A.sort()
B = [int(y) for y in input().split()]

answer = 0
for i in range(N):
    answer += A[0] * max(B)
    del A[0]
    B.pop(B.index(max(B)))

print(answer)