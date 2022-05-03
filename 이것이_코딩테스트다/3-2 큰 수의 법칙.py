"""
 입력 예시
 5 8 3
 2 4 5 4 6

 출력예시
 46
"""

N, M, K = map(int, input().split()) #N은 배열의 크기, M은 숫자가 더해지는 횟수, K번을 초과하여 더해질 수 없음
data = list(map(int, input().split()))

data.sort(reverse=True)

result = 0
second = int(M//(K+1))

if second > 0:
    result += data[1] * second
    result += data[0] * (M - second)
else:
    result += data[0] * (M - second)

print(result)
