import sys

N = int(input())
a = [int(x) for x in sys.stdin.readline().split()]
dict={}
for k in a:
    if k in dict:
        dict[k] += 1
    else:
        dict[k] = 1

n = int(input())
b = [int(x) for x in sys.stdin.readline().split()]
c=[]
for i in b:
    if i in dict:
        c.append(dict[i])
    else:
        c.append(0)

print(*(c))
