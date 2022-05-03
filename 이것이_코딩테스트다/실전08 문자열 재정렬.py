"""
입력 예시1
K1KA5CB7
출력 예시1
ABCKK13
"""

data = input()

l1 = []
l2 = 0

for i in data:
    if i.isalpha():
        l1.append(i)
    elif i.isdigit():
        l2 += int(i)

l1.sort()
print("".join(l1) + str(l2))


