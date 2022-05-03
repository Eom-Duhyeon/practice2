import sys
from collections import deque
N = int(sys.stdin.readline())

qu = deque()
for i in range(N):
    com = sys.stdin.readline().split()
    if com[0] == "push":
        qu.append(com[1])
    elif com[0] == "pop":
        if len(qu) == 0:
            print(-1)
        else:
            a = qu.popleft()
            print(a)
    elif com[0] == "size":
        print(len(qu))
    elif com[0] == "empty":
        if len(qu) ==0:
            print(1)
        else:
            print(0)
    elif com[0] == "front":
        if len(qu) == 0:
            print(-1)
        else:
            print(qu[0])
    elif com[0] == "back":
        if len(qu) == 0:
            print(-1)
        else:
            print(qu[-1])