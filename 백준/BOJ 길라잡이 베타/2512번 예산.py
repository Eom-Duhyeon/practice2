# import sys
#
# n = int(input())
# expense = [int(x) for x in sys.stdin.readline().split()]
# maxi = int(input())
#
# start = 1
# end = max(expense)
#
# if sum(expense) <= maxi:
#     print(end)
# else:
#     while start <= end:
#         num = 0
#         mid = (start+end)//2
#         for i in expense:
#             if i > mid:
#                 num += mid
#             else:
#                 num += i
#         if num > maxi:
#             end = mid - 1
#         else:
#             start = mid + 1
#
#     print(start-1)


"""
4
120 110 140 150
485

5
70 80 30 40 100
450
"""
import sys

n = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
money = int(sys.stdin.readline())

if sum(budgets) > money:
    start = 1
    end = max(budgets)
    while start <= end:
        mid = (start+end)//2
        sum_v = 0
        for budget in budgets:
            if budget >= mid:
                sum_v += mid
            else:
                sum_v += budget
        if sum_v > money:
            end = mid - 1
        else:
            start = mid + 1

    print(end)
else:
    print(max(budgets))
