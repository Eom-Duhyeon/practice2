import sys

n = int(input())
expense = [int(x) for x in sys.stdin.readline().split()]
maxi = int(input())

start = 1
end = max(expense)

if sum(expense) <= maxi:
    print(end)
else:
    while start <= end:
        num = 0
        mid = (start+end)//2
        for i in expense:
            if i > mid:
                num += mid
            else:
                num += i
        if num > maxi:
            end = mid - 1
        else:
            start = mid + 1

    print(start-1)


"""
4
120 110 140 150
485

5
70 80 30 40 100
450
"""