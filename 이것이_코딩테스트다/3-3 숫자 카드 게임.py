"""
입력 예시
3 3
3 1 2
4 1 4
2 2 2

출력 예시
2
"""

a, b = map(int, input().split()) #리스트의 행열 길이
result = 0 #
for i in range(a):
    buff = min(list(map(int,input().split())))
    result = max(buff, result2 )

print(result)