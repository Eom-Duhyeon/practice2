n = int(input())
one = [0 for i in range(n+1)]

if n==1:
    print(0)
    exit()
for i in range(2,n+1):
    one[i] = one[i-1]+1
    if i%3 == 0:
        one[i] = min(one[i], one[i//3]+1)
    if i%2 ==0:
        one[i] = min(one[i], one[i//2]+1)

print(one[n])
