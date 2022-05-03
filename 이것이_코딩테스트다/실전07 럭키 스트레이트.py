"""
입력 예시 1
123402
출력 예시1
LUCKY
입력 예시 2
7755
출력 예시 2
READY
"""


# left = 0
# right = 0
# n = list(map(int, input()))
# for i in range(len(n)//2):
#     left += n[i]
#     right += n[-(i+1)]
#
# if left == right:
#     print("LUCKY")
# else:
#     print("READY")

numbers = list(map(int, input()))

n = len(numbers)

result = 0
for i in range(n//2):
    result += numbers[i]

for i in range(n//2, n):
    result -= numbers[i]

if result == 0:
    print("LUCKY")
else:
    print("READY")