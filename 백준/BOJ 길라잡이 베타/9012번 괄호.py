import sys

N = int(input())
for i in range(N):
    com = sys.stdin.readline().strip()
    stack = []
    for j in com:
        if len(stack) == 0:
            if j == ")":
                stack.append(1)
                break
        if j == "(":
            stack.append(1)
        elif  j == ")":
            stack.pop()

    if stack:
        print("NO")
    else:
        print("YES")
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(