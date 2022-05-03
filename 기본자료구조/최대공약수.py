def gcd(a,b):
    while True:
        if b == 0:
            return a
        return gcd(b, a % b)

print(gcd(17, 15))