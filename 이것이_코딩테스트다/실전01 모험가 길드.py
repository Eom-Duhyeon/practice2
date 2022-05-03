

length = int(input())
data = list(map(int, input().split()))

data.sort()

count = 0
answer = 0
for i in data:
    count += 1
    if count >= i :
        answer += 1
        count = 0

print(answer)
