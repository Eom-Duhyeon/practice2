# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
#
# 명령은 총 여덟 가지이다.
#
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# import sys
# from collections import deque
# N = int(sys.stdin.readline())
#
# qu = deque()
# for i in range(N):
#     com = sys.stdin.readline().split()
#     if com[0] == "push_front":
#         qu.appendleft(com[1])
#     elif com[0] == "push_back":
#         qu.append(com[1])
#     elif com[0] == "pop_front":
#         if len(qu) == 0:
#             print(-1)
#         else:
#             a = qu.popleft()
#             print(a)
#     elif com[0] == "pop_back":
#         if len(qu) == 0:
#             print(-1)
#         else:
#             a = qu.pop()
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

    if command[0] == "push_front":
        qu.appendleft(command[1])
    elif command[0] == "push_back":
        qu.append(command[1])
    elif command[0] == "pop_front":
        if qu:
            print(qu.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if qu:
            print(qu.pop())
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
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front

"""