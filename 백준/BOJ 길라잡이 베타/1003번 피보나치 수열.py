
n = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]
def fibo(n):
    length = len(zero)
    if n < length:
        print(zero[n], one[n], sep=" ")
    else:
        for i in range(length, n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
        print(zero[n], one[n], sep=" ")

for i in range(n):
    fibo(int(input()))
