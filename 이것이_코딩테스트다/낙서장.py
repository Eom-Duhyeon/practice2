# import collections
#
# x, y = 1, 2
#
# q = collections.deque()
# q.append((x, y))
#
# a, b = q.popleft()
# print (a)

s="abcabc"
# pat = s[:2]
# print(pat)
# print([[0]*5]*5)
#
#
#
#
#
#
#
#
#
# def solution(key, lock):
#     n = len(lock)
#     m = len(key)
#
#     def rotate(a):
#         n = len(a)
#         m = len(a[0])
#         result = [[0] * n for _ in range(m)]
#         for i in range(n):
#             result[j][n - i - 1] = a[i][j]
#         return result
#
#     def check(new_lock):
#         lock_length = len(new_lock) // 3
#         for i in range(lock_length, lock_length * 2):
#             for j in range(lock_length, lock_length * 2):
#                 if new_lock[i][j] != 1:
#                     return False
#         return True
#
#     new_lock = [[0]*(n*3) for _ in range(n * 3)]
#     for i in range(n):
#         for j in range(n):
#             new_lock[i+n][j+n] = lock[i][j]
#
#     for rotation in range(4):
#         key = rotate(key)
#         for x in range(n*2):
#             for y in range(n*2):
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] += key[i][j]
#                 if check(new_lock) == True:
#                     return  True
#
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] -= key[i][j]
#     return  False
#
# print([[0]*3 for _ in range(3)] )

# # print((-4)%4)
# a = [[0, 0, 0, 0],[0, 0] ]
#
# print(a[1].count(0))

# ans = "abcdefghi"
# print(ans[-2:0:-1])

walls = [(0,3), (0,5), (0,8)]

for x, y in walls:
    print(x,y)