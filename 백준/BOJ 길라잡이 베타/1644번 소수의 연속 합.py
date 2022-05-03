n = int(input())

if n==1:
    print(0)
elif n==2:
    print(1)
else:
    arr = [True]*(n+1)
    prime = []
    for i in range(2, n+1):
        if arr[i] == True:
            prime.append(i)
            for j in range(2*i, n+1, i):
                arr[j] = False

    length = len(prime)
    answer = 0
    for i in range(length-1, -1, -1):
        candid = 0
        for j in range(i, -1, -1):
            candid += prime[j]
            if candid == n:
                answer += 1
                break
            elif candid > n:
                break


    print(answer)


