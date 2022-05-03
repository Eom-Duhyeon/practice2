"""
정수 x가 주어질 때 정수 x에 사용할 수 있는 연산은 다음과같이 4가지이다.
x가 5로 나누어 떨어지면, 5로 나눈다.
x가 3으로 나누어 떨어지면, 3으로 나눈다.
x가 2로 나누어떨어지면, 2로 나눈다.
x에서 1을 뺀다.
연산을 사용하는 횟수의 최솟값을 구하여라.
"""

n = int(input())

array = [0 for x in range(101)]


for i in range(2, n+1):
    array[i] = array[i-1] + 1
    if i % 2 == 0:
        array[i] = min(array[i], array[i//2]+1)
    if i % 3 == 0:
        array[i] = min(array[i], array[i//3]+1)
    if i % 5 == 0:
        array[i] = min(array[i], array[i//5]+1)

print(array[n])

