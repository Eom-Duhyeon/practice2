N = int(input())
array = []
for i in range(N):
    data = input().split()
    array.append((data[0], int(data[1])))

array.sort(key=lambda x:x[1])

for _ in array:
    print(_[0], end=" ")