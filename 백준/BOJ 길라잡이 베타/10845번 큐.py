# import sys
# from collections import deque
# N = int(sys.stdin.readline())
#
# qu = deque()
# for i in range(N):
#     com = sys.stdin.readline().split()
#     if com[0] == "push":
#         qu.append(com[1])
#     elif com[0] == "pop":
#         if len(qu) == 0:
#             print(-1)
#         else:
#             a = qu.popleft()
#             print(a)
#     elif com[0] == "size":
#         print(len(qu))
#     elif com[0] == "empty":
#         if len(qu) ==0:
#             print(1)
#         else:
#             print(0)
#     elif com[0] == "front":
#         if len(qu) == 0:
#             print(-1)
#         else:
#             print(qu[0])
#     elif com[0] == "back":
#         if len(qu) == 0:
#             print(-1)
#         else:
#             print(qu[-1])
import collections
import sys

qu = collections.deque()
for i in range(int(input())):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        qu.append(command[1])
    elif command[0] == "pop":
        if qu:
            print(qu.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(qu))
    elif command[0] == "empty":
        if qu:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if qu:
            print(qu[0])
        else:
            print(-1)
    elif command[0] == "back":
        if qu:
            print(qu[-1])
        else:
            print(-1)

"""
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
"""