"""
입력 예시1
5 3
1 3 2 3 2
출력 예시1
8
"""
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
#
# count = 0
# for i in range(n-1):
#     for j in range(i+1,n):
#         if data[i] != data[j]:
#             count += 1
#
# print(count)

length, weight = map(int, input().split())

balls = list(map(int, input().split()))

array = [0]*(weight+1)
for i in balls:
    array[i] += 1

result = 0
for i in range(1, weight+1):
    length -= array[i]
    result += array[i]*length

print(result)
