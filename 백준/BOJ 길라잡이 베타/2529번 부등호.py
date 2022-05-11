"""
2
< >
출력
897
021


예제 2
9
> < < < > > > < <
출력
9567843012
1023765489
"""

n = int(input())
signs = input().split()

used = [False]*10
ms, ml = "", ""

def check(i,j,k):
    if k == "<":
        return i<j
    else:
        return j<i

def rec(length, arr):
    global ms, ml
    if length > n:
        if len(ms) == 0:
            ms = arr[:]
        else:
            ml = arr[:]
        return

    for i in range(10):
        if not used[i]:
            if length == 0 or check(int(arr[-1]), i, signs[length-1]):
                used[i] = True
                rec(length+1, arr + str(i))
                used[i] = False

if len(ml) == 0:
    ml = ms[:]

rec(0,"")
print(ml)
print(ms)