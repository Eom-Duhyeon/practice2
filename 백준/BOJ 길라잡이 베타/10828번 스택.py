# import sys
# N = int(sys.stdin.readline())
#
# stack = []
# for i in range(N):
#     com = sys.stdin.readline().split()
#     if com[0] == "push":
#         stack.append(com[1])
#     elif com[0] == "pop":
#         if len(stack) == 0:
#             print(-1)
#         else:
#             a = stack.pop()
#             print(a)
#     elif com[0] == "size":
#         print(len(stack))
#     elif com[0] == "empty":
#         if len(stack) ==0:
#             print(1)
#         else:
#             print(0)
#     elif com[0] == "top":
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[-1])

    # 14
    # push
    # 1
    # push
    # 2
    # top
    # size
    # empty
    # pop
    # pop
    # pop
    # size
    # empty
    # pop
    # push
    # 3
    # empty
    # top
import sys

stack = []

for i in range(int(input())):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)