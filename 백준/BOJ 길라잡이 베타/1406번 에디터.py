# 먼저 커서의 위치를 숫자로 저장했다가 L, D 일 때 커서 위치를 조정하고 B, P를 수행할 때 커서를 인덱스 삼아 insert와 del을 수행한다.
# 이 방법은 시간이 초과된다. 인덱스 기반 명령어라 수행의 big O가 크다.

# import sys
#
# left = list(sys.stdin.readline().strip())
# right = []
# N = int(sys.stdin.readline())
#
# for i in range(N):
#     a = sys.stdin.readline().split()
#     if a[0] == "L" and left:
#         right.append(left.pop())
#     elif a[0] == "D" and right:
#         left.append(right.pop())
#     elif a[0] == "B" and left:
#         left.pop()
#     elif a[0] == "P":
#         left.append(a[1])
#
# print(''.join(left+list(reversed(right))))
import collections
import sys

left = list(sys.stdin.readline().strip())
right = collections.deque()

for i in range(int(input())):
    com = sys.stdin.readline().split()
    if com[0] == "L":
        if left:
            right.appendleft(left.pop())
    elif com[0] == "D":
        if right:
            left.append(right.popleft())
    elif com[0] == "B":
        if left:
            left.pop()
    elif com[0] == "P":
        left.append(com[1])

print(''.join(left+list(right)))


# abcd
# 3
# P x
# L
# P y

# abc
# 9
# L
# L
# L
# L
# L
# P x
# L
# B
# P y

# dmih
# 11
# B
# B
# P x
# L
# B
# B
# B
# P y
# D
# D
# P z

# 명령어 : L 커서를 한 칸 왼쪽으로 D 오른쪽으로 B커서 왼쪽에 있는 문자 삭제 P $ 커서 왼쪽에 문자를 삽입



