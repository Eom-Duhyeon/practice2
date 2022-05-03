from math import ceil

a, b, v = map(int, input().split())

answer = 1
if a < v:
    answer += ceil((v-a)/(a-b))

print(answer)