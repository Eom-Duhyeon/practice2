"""
2
5 6
0 0 1 0

출력 예시
30 # 최댓값
30 # 최솟값
"""
import itertools

n = int(input())
data = list(map(int, input().split()))
signs_input = list(map(int, input().split()))
#sings 0번은 + 1번은 - 2번은 x 3번은 나누기,
signs = []
for i in range(4):
    for j in range(signs_input[i]):
        signs.append((i, j))

maximum = -1*(1e9)
minimum = 1e9


for sign in itertools.permutations(signs, n-1):
    passing = False
    result = data[0]
    for i in range(n-1):
        if sign[i][0] == 0:
            result += data[i+1]
        elif sign[i][0] == 1:
            result -= data[i+1]
        elif sign[i][0] == 2:
            result *= data[i+1]
        elif sign[i][0] == 3:
            if data[i+1] == 0:
                passing = True
                break
            else:
                if result * data[i+1] < 0:
                    result = -1*(abs(result)//abs(data[i+1]))
                else:
                    result = result//data[i+1]

    if not passing:
        if result > maximum:
            maximum = result

        if result < minimum:
            minimum = result

print(maximum)
print(minimum)
