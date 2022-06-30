# import itertools
#
#
# def solution(number, k):
#     n = len(number)
#     k = n-k
#     number = [int(x) for x in number]
#     first = max(number[:n - k + 1])
#     for i in range(n):
#         if first == number[i]:
#             first = i
#             break
#
#     biggest = 0
#     for i in itertools.combinations(number[i + 1:], k - 1):
#         buf = ""
#         for j in i:
#             buf = buf + str(j)
#         if int(buf) > biggest:
#             biggest = int(buf)
#
#     biggest += number[first] * (10 ** (k - 1))
#
#     return biggest
#
#
# number = "1231234"
# k = 3
#
# print(solution(number, k))
# import itertools
#
# a = [0, 1, 1]
#
# print(list(itertools.permutations(a, 3)))

# import math
# print(math.ceil(1//2))

# a = [1, 2]
# a.insert(1, 3)
# print(a)

# n = [1, 5, "target", 3]
# print(max(n))

a = "morgan string_compare"
a = a.split()
print(a[1])