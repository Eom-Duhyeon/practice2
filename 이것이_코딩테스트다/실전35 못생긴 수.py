n = int(input())

ulgy = [0] * n
ulgy[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1,n):
    ulgy[i] = min(next2, next3, next5)
    if ulgy[i] == next2:
        i2 += 1
        next2 = ulgy[i2] * 2
    if ulgy[i] == next3:
        i3 += 1
        next3 = ulgy[i3] * 3
    if ulgy[i] == next5:
        i5 += 1
        next5 = ulgy[i5] * 5

print(ulgy[n-1])