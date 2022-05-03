"""
입력 예시
a1
출력 예시
2
"""
pos = input()
row = int(pos[1])
column = int(ord(pos[0]))-int(ord('a'))+1 #ord : 유니코드 정수 반환.

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)]

result = 0
for step in steps:
    possible_r = row + step[0]
    possible_c = column + step[1]
    if possible_c >= 1 and possible_c <= 8 and possible_r >= 1 and possible_r <= 8:
        result += 1

print(result)