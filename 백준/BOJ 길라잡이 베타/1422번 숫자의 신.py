k, n = map(int, input().split()) # k개의 입력, n개의 선택. n은 언제나 k 이상. 모든 숫자는 반드시 한 번 이상
numbers = []
for i in range(k):
    numbers.append(str(input()))

numbers.sort(key=lambda x:x*9, reverse=True)


length = len(numbers[0])
idx = 0
for i in range(1, k):
    if len(numbers[i]) > length:
        length = len(numbers[i])
        idx = i
if length == len(numbers[0]):
    answer = numbers[0] * (n - k)
    answer += str(int(''.join(numbers)))
    print(answer)
else:
    for i in range(n-k):
        numbers.insert(idx, numbers[idx])
    print(str(int(''.join(numbers))))




"""
2 4
4
7

4 9
4
4
4
4

3 4
1
10
100
"""
