# n = int(input())
# tree = []
# term = 0
# def gcd(a, b):
#     if a%b ==0:
#         return b
#     else:
#         return gcd(b, a%b)
#
# for i in range(n):
#     tree.append(int(input()))
#
# tree.sort()
#
# term = tree[1] - tree[0]
# for i in range(1,n-1):
#     inter = tree[i+1] - tree[i]
#     term = gcd(max(term, inter),min(term, inter))
#
# print(int((tree[-1]-tree[0])/term -(n-1)))

n = int(input())
trees = []
for i in range(n):
    trees.append(int(input()))
trees.sort()

def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

term = trees[1] - trees[0]


#틀렸던 이유: 모든 간격에 대해 조사해야 한다. ex) 간격 2, 4, 7인 경우 2,4만 비교하면 2가 되지면 7도 비교하면 1이 된다.
for i in range(2, n):
    inter = trees[i] - trees[i-1]
    term = gcd(max(inter, term), min(inter, term))

print(int((trees[-1]-trees[0])/term - n +1))
