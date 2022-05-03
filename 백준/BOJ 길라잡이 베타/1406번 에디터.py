import sys

left = list(sys.stdin.readline().strip())
right = []
N = int(sys.stdin.readline())

for i in range(N):
    a = sys.stdin.readline().split()
    if a[0] == "L" and left:
        right.append(left.pop())
    elif a[0] == "D" and right:
        left.append(right.pop())
    elif a[0] == "B" and left:
        left.pop()
    elif a[0] == "P":
        left.append(a[1])

print(''.join(left+list(reversed(right))))

# abcd
# 3
# P x
# L
# P y