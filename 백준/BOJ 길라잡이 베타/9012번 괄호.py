# import sys
#
# N = int(input())
# for i in range(N):
#     com = sys.stdin.readline().strip()
#     stack = []
#     for j in com:
#         if len(stack) == 0:
#             if j == ")":
#                 stack.append(1)
#                 break
#         if j == "(":
#             stack.append(1)
#         elif  j == ")":
#             stack.pop()
#
#     if stack:
#         print("NO")
#     else:
#         print("YES")

for i in range(int(input())):
    cnt = 0
    u = input()
    bo = True
    for i in u:
        if i == "(":
            cnt += 1
        else:
            if cnt == 0:
                bo = False
                break
            else:
                cnt -= 1
    if cnt != 0:
        bo = False
    if bo:
        print("YES")
    else:
        print("NO")

# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(