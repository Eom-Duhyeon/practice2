"""
입력 예시1
02984
출력 예시1
576
"""



array = list(map(int, input()))
result = array[0]

for i in range(1, len(array)):
    new = int(array[i])
    if result == 0 or new == 0:
        result += new
    else:
        result *= new

print(result)