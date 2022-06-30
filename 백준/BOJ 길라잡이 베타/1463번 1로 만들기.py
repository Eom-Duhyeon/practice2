# n = int(input())
# one = [0 for i in range(n+1)]
#
# if n==1:
#     print(0)
#     exit()
# for i in range(2,n+1):
#     one[i] = one[i-1]+1
#     if i%3 == 0:
#         one[i] = min(one[i], one[i//3]+1)
#     if i%2 ==0:
#         one[i] = min(one[i], one[i//2]+1)
#
# print(one[n])

"""
입력 : 10
출력 : 3
"""

# 미리 n-1을 입력하는 것은 안 좋은 생각이다. 다이나믹 프로그래밍이라 n-1값이 언제든지 바뀐다는 것을 생각하자.

n = int(input())
num = [0]*(n+1)

for i in range(2, n+1):
    num[i] = num[i-1] + 1
    if not i % 3:
        num[i] = min(num[i], num[i//3] + 1)
    if not i % 2:
        num[i] = min(num[i], num[i//2] + 1)

print(num[n])