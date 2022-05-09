import sys

n = int(input())
primes = []
nums = [False, False] + [True for _ in range(1500000-2)]
for i in range(2, 1500000):
    if nums[i] == True:
        primes.append(i)
        for j in range(i*2, 1500000, i):
            nums[j] = False

def isPrime(s):
    if s > 1500000 - 1:
        for prime in primes:
            if s % prime == 0:
                return False
        return True
    else:
        return nums[s]


for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    s = a + b
    if s < 4:
        print("NO")
    else:
        if (a + b) % 2 == 0:
            print("YES")
        else:
            # 모든 소수는 2를 제외하면 홀수이다. 즉 a+b - 2가 홀수인지 판단하면 된다.
            s -= 2
            if isPrime(s):
                print("YES")
            else:
                print("NO")










