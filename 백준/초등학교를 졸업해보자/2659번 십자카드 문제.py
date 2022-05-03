def fin_clock_num(num):
    clocknum = num

    for i in range(0,4):
        num= num // 1000 + (num % 1000) * 10
        if clocknum > num:
            clocknum = num

    return clocknum

n = int(''.join(input().split()))

clocknum = fin_clock_num(n)

start = 1111
count = 0

while (start <= clocknum):
    if fin_clock_num(start) == start:
        count += 1
    start += 1

print(count)